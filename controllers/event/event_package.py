from odoo import http
from odoo.http import request
from odoo.http import request as req
from werkzeug.utils import redirect
from datetime import date, time, datetime


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


class AsEventPackage(http.Controller):
    @http.route('/event/package/detail', type="http", auth='public')
    def event_package_detail(self, **kw):

        event_id = kw.get('id')
        if not event_id:
            return 'Event id not passed'

        currency = req.env.company.currency_id
        event = req.env['as.event'].sudo().search([('id', '=', int(event_id))])

        return req.render('as_rental.event_package_detail', {
            'event': event,
            'currency': currency,
            'date_today': date.today(),
        })

    @http.route('/event/package/payment', type="http", auth='public')
    def event_package_payment(self, **kw):
        event_id = kw.get('event_id')
        event_package_date = kw.get('event-package-date')
        if not event_id or not event_package_date:
            return 'event_id or event_package_date not passed'

        pt = get_partner_obj()
        if not pt:
            req.session['redirect'] = f'/event/package/payment?event_id=17&event-package-date={event_package_date}'
            return redirect(f"/web/login?service_type=event_package&event_id={event_id}")

        # Clear redirect
        req.session['redirect'] = None

        currency = req.env.company.currency_id
        event = req.env['as.event'].sudo().search([('id', '=', int(event_id))])

        if not event and not currency:
            return 'Event object or currency not found'

        return req.render('as_rental.event_package_payment', {
            'currency': currency,
            'event': event,
            'event_package_date': event_package_date,
        })

    @http.route('/event/package/payment/process', type="http", auth='public')
    def event_package_payment_process(self, **kw):
        event_id = kw.get('event_id')
        event_package_date = kw.get('event_package_date')
        if not event_id or not event_package_date:
            return 'Event ID or event_package_date not passed'

        print('event_id', event_id)

        # Check login
        pt = get_partner_obj()
        if not pt:
            return redirect('/web/login')

        # Event
        event = req.env['as.event'].sudo().search([('id', '=', int(event_id))])
        if not event:
            return 'Event object not found'

        # Search event registration product
        product_id = req.env['product.product'].sudo().search([('default_code', '=', 'EVENT_REGISTRATION')], limit=1)
        if not product_id:
            return 'EVENT_REGISTRATION product not found'

        so_values = {
            'partner_id': pt.id,
            'order_line': [
                (0, 0, {
                    'product_id': product_id.id,
                    'product_uom_qty': 1.0,
                    'name': f'{event.name} (Tour Date: {event_package_date})',
                    # 'price_unit': 100.00,
                    'tax_id': False,
                })]
        }
        so = req.env['sale.order'].sudo().create(so_values)
        if not so:
            return 'SO was not created'

        # Todo: Activities on Event package sale done
        notification = req.env['as.notification'].sudo().create({
            'partner_id': pt.id,
            'notification': 'Your Event package order has been successfully placed',
        })

        return redirect(f'/event/package/payment/confirmation?so_id={so.id}&event_id={event.id}')

    @http.route('/event/package/payment/confirmation', type="http", auth='public')
    def event_package_payment_confirmation(self, **kw):
        currency = req.env.company.currency_id
        so_id_str = kw.get('so_id')
        event_id_str = kw.get('event_id')

        if not so_id_str:
            return 'SO ID Not found'

        so_id = req.env['sale.order'].sudo().search([('id', '=', int(so_id_str))])
        if not so_id:
            return 'SO Object Not found'

        if not so_id_str:
            return 'SO ID Not found'

        event_id = req.env['as.event'].sudo().search([('id', '=', int(event_id_str))])
        if not event_id:
            return 'Event Object Not found'

        return req.render('as_rental.event_package_confirmation', {
            'currency': currency,
            'so': so_id,
            'event_id': event_id,
        })
