from odoo import http
from odoo.http import request
from odoo.http import request as req
from werkzeug.utils import redirect
from datetime import date, time, datetime
# import datetime
# import base64


def get_partner_id():
    uid = http.request.env.user.id
    pid = http.request.env['res.users'].sudo().search([('id', '=', uid)]).partner_id.id
    if pid:
        return pid
    else:
        return None


def get_partner_obj():
    uid = http.request.env.user.id
    pid = http.request.env['res.users'].sudo().search([('id', '=', uid)]).partner_id
    if pid:
        return pid
    else:
        return None


class AsEvent(http.Controller):
    @http.route('/event', type="http", auth='public')
    def event(self, **kw):
        pt = get_partner_obj()
        date_today = date.today()
        domain = [
            ('published', '=', True),
            # ('date_end', '>=', date_today),
        ]

        currency = req.env.company.currency_id
        categories = req.env['as.event_category'].sudo().search([])

        # Render by filter (Check if page is filtered)
        # Add new rule to domain
        category = kw.get('category')
        if category and not category == 'all':
            category_ids = int(category)
            domain.append(('category_ids', 'in', category_ids))

        # Get events by domain
        events = req.env['as.event'].sudo().search(domain)

        """
        ===================================================================
        # Event search: If user search for events
        ===================================================================
        """
        if kw.get('event-search'):

            # Store search
            search = req.env['as.search'].sudo().create({
                'area': 'EVENT',
                'query': kw.get('event-search'),
                'partner_id': pt.id if pt else None,
            })

            search_events = []
            search_domain = [
                ('published', '=', True),
                # ('date_end', '>=', date_today),
            ]
            search_event_objects = req.env['as.event'].sudo().search(search_domain)
            print('search_event_objects', search_event_objects)

            # Process user query
            user_query = kw.get('event-search')
            user_query = user_query.strip(' ')
            query_list = user_query.split(' ')

            # Process event filtering
            event_string = ''
            for event in search_event_objects:
                event_string = f'{event.name} {event.destination}'
                event_string = event_string.lower()

                for query in query_list:
                    _query = query.lower()
                    if _query in event_string and event not in search_events:
                        search_events.append(event)

            # Now replace current events if match from search
            events = search_events

        filter_events = []
        for event in events:
            if not event.package:
                if event.date_end and event.date_end >= date_today:
                    filter_events.append(event)
                    print('Normal')
            else:
                filter_events.append(event)
                print('Package')

        return req.render('as_rental.event', {
            'events': filter_events,
            'currency': currency,
            'categories': categories,
            'kw': kw,
        })

    @http.route('/event/detail', type="http", auth='public')
    def event_detail(self, **kw):

        event_id = kw.get('id')
        if not event_id:
            return 'Event id not passed'

        currency = req.env.company.currency_id
        event = req.env['as.event'].sudo().search([('id', '=', int(event_id))])

        seat_full = False
        maximum_attendees = event.maximum_attendees
        event_ticket_ids = event.event_ticket_ids
        seats_available = maximum_attendees

        if event_ticket_ids:
            seats_available = maximum_attendees - len(event_ticket_ids)
            if seats_available < 1:
                seat_full = True

        print('maximum_attendees', maximum_attendees)
        print('event_ticket_ids', event_ticket_ids)
        print('seats_available', seats_available)
        print('seats_available', type(seats_available))

        return req.render('as_rental.event_detail', {
            'event': event,
            'currency': currency,
            'seats_available': seats_available,
            'seat_full': seat_full,
        })

    @http.route('/event/ticket', type='http', auth='public')
    def event_ticket(self, **kw):
        pt = get_partner_obj()
        event_id = kw.get('id')

        # Check user login
        if not pt:
            req.session['redirect'] = f'/event/ticket?id={event_id}'
            return redirect(f"/web/login?service_type=event&event_id={event_id}")

        # Clear redirect
        req.session['redirect'] = None

        if not event_id:
            return 'Event id not found'

        event_id = int(event_id)

        return req.render('as_rental.event_ticket', {
            'event_id': event_id,
            'kw': kw,
        })

    @http.route('/event/ticket-process', type='http', csrf=False)
    def event_ticket_process(self, **kw):

        """
        Process ticket
        Process ticket
        """
        print(kw)
        num_of_ticket = kw.get('num_of_ticket')
        event_id = kw.get('event_id')

        if not kw and not num_of_ticket and not event_id:
            return 'Value missing'

        num_of_ticket = int(num_of_ticket)
        event_id = int(event_id)

        if num_of_ticket < 1:
            return 'Invalid quantity'

        # Set ticket count to session
        req.session['num_of_ticket'] = num_of_ticket
        req.session['event_id'] = event_id

        tickets = []
        # ticket[0] is enumerate index like 1, 2, 3, 4, 5 etc
        for ticket in enumerate(range(num_of_ticket), start=1):
            vals = {
                'name': kw.get(f'ticket{ticket[0]}__name') or '-',
                'phone': kw.get(f'ticket{ticket[0]}__phone') or '-',
            }
            tickets.append(vals)

        # add tickets to session
        print('tickets:', tickets)
        req.session['tickets'] = tickets

        # ==============================
        # Add event product to cart
        # ==============================

        # Get product id of Event Registration
        event_reg_pd = req.env['product.template'].sudo().search([('default_code', '=', 'EVENT_REGISTRATION')], limit=1)
        if not event_reg_pd:
            return '"EVENT_REGISTRATION" Product not found'

        # Update event product price
        event = req.env['as.event'].sudo().search([('id', '=', event_id)], limit=1)
        if not event:
            return 'Event not found'
        event_reg_pd.list_price = event.list_price

        # Update cart
        cart = [
            {
                'product_id': event_reg_pd.id,
                'quantity': num_of_ticket,
            }
        ]
        req.session['cart'] = cart

        return redirect('/payment')

    # event payment
    @http.route('/payment', type="http", auth='public')
    def payment(self, **kw):

        # This block currently used in event only
        # property cart is different
        cart = req.session.get('cart')
        cart_items = []
        total = 0.0

        if not cart:
            return redirect('/')

        for item in cart:

            product_tmpl_id = item.get('product_id')
            quantity = item.get('quantity')
            product_tmpl = req.env['product.template'].sudo().search([('id', '=', product_tmpl_id)])

            if not product_tmpl:
                return

            vals = {
                'product_id': product_tmpl,
                'quantity': quantity,
                'price': product_tmpl.list_price * quantity,
            }

            cart_items.append(vals)
            total = total + (product_tmpl.list_price * quantity)

        print(cart_items)
        print(total)
        currency = req.env.company.currency_id

        # Get event object
        event = None
        event_id = req.session.get('event_id')
        num_of_ticket = req.session.get('num_of_ticket')
        if event_id:
            event = req.env['as.event'].sudo().search([('id', '=', event_id)])

        return req.render('as_rental.payment', {
            'cart_items': cart_items,
            'total': total,
            'currency': currency,
            'event': event,
        })

    # event /payment/process
    @http.route('/payment/process', type="http", auth='public')
    def payment_process(self, **kw):

        # Check login
        pt = get_partner_obj()
        if not pt:
            return redirect('/web/login')

        order_line = []
        cart = req.session.get('cart')

        if cart:
            for item in cart:
                product_tmpl_id = item.get('product_id')
                quantity = item.get('quantity')
                product_id = req.env['product.product'].sudo().search([('product_tmpl_id', '=', product_tmpl_id)])

                if product_id:
                    order_line.append((0, 0, {
                        'product_id': product_id.id,
                        'product_uom_qty': quantity,
                        'tax_id': False,
                    }))

        so_vals = {
            'partner_id': pt.id,
            'order_line': order_line
        }
        so = req.env['sale.order'].sudo().create(so_vals)

        if not so:
            return 'Something went wrong'

        # Event (Check if it is event/ticket product
        num_of_ticket = req.session['num_of_ticket']
        event_id = req.session['event_id']
        tickets = req.session['tickets']

        if num_of_ticket and event_id and tickets:
            ev = req.env['as.event'].sudo().search([('id', '=', event_id)])
            reg_ids = []

            if not ev:
                return 'Event object not found'

            for reg_id in ev.event_ticket_ids:
                reg_ids.append(reg_id.id)

            # for reg in range(num_of_ticket):
            for reg in tickets:
                ev_reg_vals = {
                    'responsible_id': pt.id,
                    'name': reg.get('name'),
                    'mobile': reg.get('phone'),
                    'order_id': so.id,
                }
                ev_reg = req.env['as.event_registration'].sudo().create(ev_reg_vals)
                if ev_reg:
                    reg_ids.append(ev_reg.id)

            ev.event_ticket_ids = reg_ids

            # clear event related session
            req.session['num_of_ticket'] = None
            req.session['event_id'] = None
            req.session['cart'] = None
            req.session['tickets'] = None

        """
        if tickets do something
        
        tickets = req.session.get('tickets')
        if tickets:
            event_id = req.env['as.event'].sudo().search([('id', '=', 1)])

            for ticket in tickets:
                vals = {
                    'name': ticket.get('name'),
                    'mobile': ticket.get('mobile')
                }
                evnt_reg_id = req.env['as.event_registration'].sudo().create(vals)

            if evnt_reg_id:
                ev_ids_id = event_id.event_ticket_ids
                ev_ids = []
                for ev_id in ev_ids_id:
                    ev_ids.append(ev_id.id)

                ev_ids.append(evnt_reg_id.id)
                event_id.event_ticket_ids = ev_ids
        """

        return redirect(f'/confirmation?id={so.id}')

    @http.route('/confirmation', type="http", auth='public')
    def confirmation(self, **kw):
        if not kw.get('id'):
            return 'ID not found'

        soid = int(kw.get('id'))
        so = req.env['sale.order'].sudo().search([('id', '=', soid)])
        if not so:
            return 'SO not found'

        currency = req.env.company.currency_id

        return req.render('as_rental.confirmation', {
            'so': so,
            'currency': currency,
        })
