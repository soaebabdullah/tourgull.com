from odoo import http
from odoo.http import request
from odoo.http import request as req
from werkzeug.utils import redirect
from datetime import date, time, datetime, timedelta
from odoo.tests.common import Form
from odoo.exceptions import AccessError, UserError, AccessDenied
import requests
import json


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


class AsAjax(http.Controller):

    # Asynchronous javascript and xml (ajax)

    @http.route('/get-place-category', type="http", auth='public', cors='*', csrf=False)
    def get_place_category(self, **kw):
        print('-------')
        print(kw)

        result = None
        place_id = kw.get('place_id')
        if not place_id:
            print('error')
            return 'error'

        place_id = int(place_id)
        print(f'place_id:{place_id}')
        place_categories = req.env['as.place_category'].sudo().search([('parent_id', '=', place_id)])
        print(f'place_categories:{place_categories}')

        if place_categories:
            my_place_categories = []
            for place_category in place_categories:
                vals = {
                    'id': place_category.id,
                    'name': place_category.name,
                }
                # my_place_categories.append(place_category.name)
                my_place_categories.append(vals)
            result = json.dumps(my_place_categories)
            print(f'result:{result}')
        else:
            result = 'no_result'
            print('no_result')

        return result

    # Edited By Umme Huzaifa
    # Add Search Availability
    @http.route('/check_availability', type="http", auth='public', csrf=False)
    def check_availability(self, **kw):
        """pid = kw.get("pd_id")
        checkin = kw.get("checkin")
        checkout = kw.get("checkout")

        bookings = req.env['rent.property.book'].sudo().search([
            ('product', '=', int(pid)),
            ('state', '=', 'confirm'),
        ])

        guest_check_in_date = datetime.strptime(checkin, '%Y-%m-%d').date()
        guest_check_out_date = datetime.strptime(checkout, '%Y-%m-%d').date()
        product_in_booking = False
        top_check_in = None
        top_check_out = None

        print('-----------------------')
        for booking in bookings:

            # top check_in
            if not top_check_in and booking.check_in:
                top_check_in = booking.check_in
            if top_check_in and booking.check_in and top_check_in > booking.check_in:
                top_check_in = booking.check_in

            # top check_out
            if not top_check_out and booking.check_out:
                top_check_out = booking.check_out
            if top_check_out and top_check_out < booking.check_out:
                top_check_out = booking.check_out

            # Normal mass
            if guest_check_in_date >= booking.check_in and guest_check_out_date <= booking.check_out:
                print('Booked')
                product_in_booking = True

            # check_out side mass
            elif guest_check_in_date < booking.check_out and guest_check_out_date >= booking.check_out:
                print('Booked - check_out side mass')
                product_in_booking = True

            # check_in side mass
            elif guest_check_in_date < booking.check_in and guest_check_out_date > booking.check_in:
                print('Booked - check_in side mass')
                product_in_booking = True

            # top check_in/check_out
            elif guest_check_in_date < top_check_in and guest_check_out_date > top_check_out:
                print('Booked - top check_in/check_out mass')
                product_in_booking = True

            else:
                print('Not Booked')

        print('-----------------------')
        print('product_in_booking:', product_in_booking)
        print('-----------------------')
        print('top_check_in', top_check_in)
        print('top_check_out', top_check_out)
        print('-----------------------')

        result = {
            'status': '0'
        }
        result = json.dumps(result)
        return result"""

        pid = kw.get("pd_id")
        checkin = kw.get("checkin")
        checkout = kw.get("checkout")
        rooms = kw.get("rooms")
        adults = kw.get("adults")
        children = kw.get("children")
        result = {
            'status': '0'
        }

        if checkin and checkout:
            domain = [
                ('rp_is_host_prop', '=', True),
                ('rp_start_date', '<=', checkin),
                ('rp_end_date', '>=', checkout),
                # ('rp_is_book', '=', False),
                ('id', '=', pid)
            ]

        if kw.get('rooms') and not kw.get('rooms') == '0':
            domain.append(('rp_bedrooms', '=', rooms))

        if kw.get('adults') and not kw.get('adults') == '0':
            domain.append(('rp_adults', '=', adults))

        if kw.get('children') and not kw.get('children') == '0':
            domain.append(('rp_childs', '=', children))

        # On product found
        available_product = request.env['product.template'].sudo().search(domain)
        print("available_product: ", available_product)

        # Check if product in booking or not
        product_in_booking = False

        if available_product:

            bookings = req.env['rent.property.book'].sudo().search([
                ('product', '=', int(pid)),
                ('state', '=', 'confirm'),
            ])

            guest_check_in_date = datetime.strptime(checkin, '%Y-%m-%d').date()
            guest_check_out_date = datetime.strptime(checkout, '%Y-%m-%d').date()
            top_check_in = None
            top_check_out = None

            print('-----------------------')
            for booking in bookings:

                # top check_in
                if not top_check_in and booking.check_in:
                    top_check_in = booking.check_in
                if top_check_in and booking.check_in and top_check_in > booking.check_in:
                    top_check_in = booking.check_in

                # top check_out
                if not top_check_out and booking.check_out:
                    top_check_out = booking.check_out
                if top_check_out and top_check_out < booking.check_out:
                    top_check_out = booking.check_out

                # Normal mass
                if guest_check_in_date >= booking.check_in and guest_check_out_date <= booking.check_out:
                    print('Booked')
                    product_in_booking = True

                # check_out side mass
                elif guest_check_in_date < booking.check_out and guest_check_out_date >= booking.check_out:
                    print('Booked - check_out side mass')
                    product_in_booking = True

                # check_in side mass
                elif guest_check_in_date < booking.check_in and guest_check_out_date > booking.check_in:
                    print('Booked - check_in side mass')
                    product_in_booking = True

                # top check_in/check_out
                elif guest_check_in_date < top_check_in and guest_check_out_date > top_check_out:
                    print('Booked - top check_in/check_out mass')
                    product_in_booking = True

                else:
                    print('Not Booked')

            print('-----------------------')
            print('product_in_booking:', product_in_booking)
            print('-----------------------')
            print('top_check_in', top_check_in)
            print('top_check_out', top_check_out)
            print('-----------------------')

        # Action on product found
        print("---------------------")
        if available_product and not product_in_booking:
            print("finally book_available")
            # razzak
            obj_1 = datetime.strptime(checkin, '%Y-%m-%d')
            obj_2 = datetime.strptime(checkout, '%Y-%m-%d')
            delta = obj_2 - obj_1
            nights = delta.days
            # end razzak

            # result = '1'
            result = {
                'status': '1',
                'nights': nights,
            }

        else:

            # Action on product not found
            print("product not available")
            # result = '0'
            result = {
                'status': '0'
            }

        if checkin == checkout:
            result = {
                'status': '0'
            }

        result = json.dumps(result)
        return result

    # Load more products - 04 Jan 2023
    @http.route('/load_products', type="http", auth='public', csrf=False)
    def load_products(self, **kw):

        # print(f'load_products kw:{kw}')
        result = None

        # Check pagination request
        str_page = kw.get('page')
        if not str_page or str_page == '0':
            return 'no_result'

        # Get available rental properties
        product_ids = []
        products_obj = req.env['product.template'].sudo().search([
            ('rp_is_host_prop', '=', True),  # Rental property
            ('rp_is_book', '=', False),  # Not booked
        ])

        today_date = date.today()

        # filter products with start date, end date, all-time
        for product in products_obj:
            start_date = product.rp_start_date
            end_date = product.rp_end_date

            # for unlimited product
            if not start_date or not end_date:
                product_ids.append(product.id)
                continue

            # Check date expiration (Greater than today's date)
            if today_date <= end_date:
                product_ids.append(product.id)

        # Get products objects from selected ids
        products = req.env['product.template'].sudo().search([
            ('id', 'in', product_ids),
        ])

        # print(f'products:{products}')

        # Get current page products
        page = int(str_page) - 1
        print('----------')
        print(f'page:{page}')
        load_product = 16  # Todo: changeable
        first_loaded = 32  # Todo: changeable
        offset = first_loaded + (load_product * page)
        api_products = products[offset:offset + load_product]
        # print(f'api_products:{api_products}')

        # Prepare for json dump
        if not api_products:
            return 'no_result'

        api_product_list = []
        for api_product in api_products:
            vals = {
                'id': api_product.id,
                'name': api_product.name,
                'rp_place_categ_id': api_product.rp_place_categ_id.name if api_product.rp_place_categ_id else '',
                'rp_adults': api_product.rp_adults,
                'rp_childs': api_product.rp_childs,
                'rp_city': api_product.rp_city,
                'rp_bedrooms': api_product.rp_bedrooms,
                'rp_beds': api_product.rp_beds,
                'rp_bathrooms': api_product.rp_bathrooms,
                'list_price': api_product.list_price,
            }
            api_product_list.append(vals)

        # for x in api_product_list:
        #     print(x.get('name'))
        result = json.dumps(api_product_list)
        # print(f'result:{result}')

        # Return json string to front-end
        return result

    # Get Image viewer images
    @http.route('/get_product_images', type="http", auth='public', csrf=False)
    def get_product_images(self, **kw):
        print(kw)
        pid = kw.get('pid')
        result = None

        if not pid:
            return 'no_result'

        pd = req.env['product.template'].sudo().search([('id', '=', int(pid))])
        if not pd:
            return 'no_result'

        urls = []

        if pd.image_512:
            urls.append(f'/web/image/product.template/{pd.id}/image_512')

        if pd.rp_image_2_512:
            urls.append(f'/web/image/product.template/{pd.id}/rp_image_2_512')

        if pd.rp_image_3_512:
            urls.append(f'/web/image/product.template/{pd.id}/rp_image_3_512')

        if pd.rp_image_4_512:
            urls.append(f'/web/image/product.template/{pd.id}/rp_image_4_512')

        if pd.rp_image_5_512:
            urls.append(f'/web/image/product.template/{pd.id}/rp_image_5_512')

        # More images
        if pd.rp_image_ids:
            for image in pd.rp_image_ids:
                urls.append(f'/web/image/as.image/{image.id}/image_512')

        result = json.dumps(urls)

        print('Calling /get_product_images')
        print(f'result:{result}')
        return result

    @http.route('/seen-notifications', type="http", auth='public', csrf=False)
    def seen_notifications(self, **kw):
        print('seen_notifications')

        pt = get_partner_obj()
        if not pt:
            return '0'

        # Set notifications to seen
        nts = req.env['as.notification'].sudo().search([
            ('partner_id', '=', pt.id),
            ('seen', '=', False),
        ])

        for nt in nts:
            nt.seen = True

        return '1'

    @http.route('/get-hotel-rooms', type="http", auth='public', cors='*', csrf=False)
    def get_hotel_rooms(self, **kw):

        print('kw', kw)
        final_results = None

        hotel_id = kw.get('hotel_id')
        if not hotel_id:
            final_result = 'no_result'
            return final_result

        objects = req.env['product.template'].sudo().search([('rp_hotel', '=', int(hotel_id))])
        print('objects', objects)

        if not objects:
            final_result = 'no_result'
            return final_result

        results = []
        for _object in objects:
            values = {
                'id': _object.id,
                'name': _object.name,
            }
            results.append(values)
        final_results = json.dumps(results)

        return final_results

    # Add/remove from wishlist
    @http.route('/wishlist/hotel', type="http", auth='public', website=True, csrf=False)
    def wishlist_add(self, **kw):

        print('kw', kw)
        pt = get_partner_obj()
        hotel_id = kw.get('hotel_id')

        if not hotel_id:
            return 'error'

        hotel_id = int(hotel_id)

        if not pt:
            return 'guest'

        # Search for already listed or not
        type_id = req.env['as.service'].sudo().search([('code', '=', 'hotel')], limit=1)
        wishlist = None

        if type_id:
            print('type_id', type_id)
            type_id = type_id.id
            wishlist = req.env['as.wishlist'].sudo().search([
                ('type', '=', type_id),
                ('record_id', '=', hotel_id),
            ])
            print('wishlist', wishlist)

        # Listed, So remove from wishlist
        if wishlist:
            if wishlist.unlink():
                return 'unlink'

        # Not already Listed, So add to wishlist
        else:
            values = {
                'partner_id': pt.id,
                'type': type_id,
                'record_id': hotel_id
            }
            if req.env['as.wishlist'].sudo().create(values):
                return 'create'

        return '0'
