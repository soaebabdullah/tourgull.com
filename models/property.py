"""
Models for hotel
"""
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class AsHotel(models.Model):
    _name = 'as.hotel'
    _description = 'as.hotel'

    # What's the name of your property?
    name = fields.Char(string='Name')
    star = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    ])

    # What are the contact details for this property?
    contact_name = fields.Char(string='Contact Name')
    contact_phone = fields.Char(string='Contact Phone')
    contact_phone_alternative = fields.Char(string='Contact Phone Alternative')
    contact_company_name = fields.Char(string='Contact Company Name')

    # Where's your property located?
    street = fields.Char(string='Address')
    street2 = fields.Char(string='Address')
    country_id = fields.Many2one('res.country', string='Country')
    city = fields.Char(string='City')
    zip = fields.Char(string='Zip')

    # Layout & Pricing
    # Skip

    """
    Facilities & services
    Parking
    """
    parking_is_available_to_guests = fields.Selection([
        ('no', 'No'),
        ('yes_paid', 'Yes Paid'),
        ('yes_free', 'Yes Free'),
    ], default='no', string='Parking is available to guests')
    parking_guests_reserve_required = fields.Selection([
        ('reservation_needed', 'Reservation Needed'),
        ('no_reservation_needed', 'No Reservation Needed'),
    ], default='reservation_needed', string='Parking guests reserve required')
    parking_space = fields.Selection([
        ('private', 'Private'),
        ('public', 'Public'),
    ], default='private', string='Parking space')
    parking_location = fields.Selection([
        ('on_site', 'On site'),
        ('off_site', 'Off site'),
    ], default='on_site')
    parking_price = fields.Float('Parking Price')

    """
    Facilities & services
    Breakfast
    """
    breakfast_available = fields.Selection([
        ('no', 'No'),
        ('yes_price', 'Yes, It\'s included in the price'),
        ('yes_optional', 'No, It\'s optional'),
    ], default='no', string='Breakfast available')
    breakfast_price = fields.Float()
    breakfast_type = fields.Many2one('hotel.breakfast_type')


    # Unaligned
    published = fields.Boolean(default=True)
    amenities = fields.Many2many('as.hotel.amenities', string='Amenities')
    maps_location = fields.Char(string='Maps Location')
    about_us = fields.Text(string='About Us')
    about_area = fields.Text(string='About Area')
    language_ids = fields.Many2many('res.lang', string='Languages')
    latitude = fields.Char(string='Latitude')
    longitude = fields.Char(string='Longitude')
    check_in = fields.Char('Check In (24 hour)')
    check_out = fields.Char('Check Out (24 hour)')
    age_restriction = fields.Integer(string='Age Restriction')
    accept_payment_methods = fields.Many2many('as.hotel.accept_payment_method', string='Accept Payment Methods')
    free_self_parking = fields.Boolean(string='Free self parking')
    discount = fields.Integer()

    # ======================================================================
    # static_map, Why should, Images
    # ======================================================================
    static_map_1920 = fields.Image(string='Static Map', max_width=1920, max_height=1920)
    static_map_310_174 = fields.Image(string='Static Map', related="static_map_1920", max_width=310, max_height=174)

    # Why should
    why_you_should_stay_title_1 = fields.Char(string='Title 01')
    why_you_should_stay_description_1 = fields.Text(string='Description 01')
    why_you_should_stay_title_2 = fields.Char(string='Title 02')
    why_you_should_stay_description_2 = fields.Text(string='Description 02')
    why_you_should_stay_title_3 = fields.Char(string='Title 03')
    why_you_should_stay_description_3 = fields.Text(string='Description 03')

    # Images
    cover_1920 = fields.Image(string='cover 01', max_width=1920, max_height=1920, required=True)
    cover_1024 = fields.Image("Image 1024", related="cover_1920", max_width=1024, max_height=1024, store=True)
    cover_512 = fields.Image("Image 512", related="cover_1920", max_width=512, max_height=512, store=True)
    cover_256 = fields.Image("Image 256", related="cover_1920", max_width=256, max_height=256, store=True)

    cover2_1920 = fields.Image(string='cover 02', max_width=1920, max_height=1920, required=True)
    cover2_1024 = fields.Image("Image 1024", related="cover2_1920", max_width=1024, max_height=1024, store=True)
    cover2_512 = fields.Image("Image 512", related="cover2_1920", max_width=512, max_height=512, store=True)
    cover2_256 = fields.Image("Image 256", related="cover2_1920", max_width=256, max_height=256, store=True)

    cover3_1920 = fields.Image(string='cover 03', max_width=1920, max_height=1920, required=True)
    cover3_1024 = fields.Image("Image 1024", related="cover3_1920", max_width=1024, max_height=1024, store=True)
    cover3_512 = fields.Image("Image 512", related="cover3_1920", max_width=512, max_height=512, store=True)
    cover3_256 = fields.Image("Image 256", related="cover3_1920", max_width=256, max_height=256, store=True)

    cover4_1920 = fields.Image(string='cover 04', max_width=1920, max_height=1920, required=True)
    cover4_1024 = fields.Image("Image 1024", related="cover4_1920", max_width=1024, max_height=1024, store=True)
    cover4_512 = fields.Image("Image 512", related="cover4_1920", max_width=512, max_height=512, store=True)
    cover4_256 = fields.Image("Image 256", related="cover4_1920", max_width=256, max_height=256, store=True)


class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'hotel.room'

    # General
    hotel_id = fields.Many2one('as.hotel', string='Hotel')
    type = fields.Selection([
        ('single', 'Single'),
        ('double', 'Double'),
        ('twin', 'Twin'),
        ('twin_double', 'Twin_double'),
        ('triple', 'Triple'),
        ('quad', 'Quad'),
        ('family', 'Family'),
        ('suite', 'Suite'),
        ('studio', 'Studio'),
        ('apartment', 'Apartment'),
        ('dorm_room', 'Dorm room'),
        ('bed_in_dorm', 'Bed in dorm'),
    ])
    name_id = fields.Many2one('hotel.room_name', string='Room Name')
    custom_name = fields.Char()
    num_rooms = fields.Integer()

    # Bed Options


    # Room size (optional)
    size = fields.Integer()
    meas_unit = fields.Selection([
        ('square_meter', 'Square meter'),
        ('square_feet', 'Square feet'),
    ])

    # Base price per night
    price = fields.Float()


class HotelRoomName(models.Model):
    _name = 'hotel.room_name'
    _description = 'hotel.room_name'
    _rec_name = 'name'

    name = fields.Char(required=True)
    code = fields.Char()


class ClassName(models.Model):
    _name = 'hotel.room_bed_type'
    _description = 'hotel.room_bed_type'
    _rec_name = 'name'

    name = fields.Char()
    capacity = fields.Integer(help='Suggested person capacity')


class HotelBreakFastType(models.Model):
    _name = 'hotel.breakfast_type'
    _description = 'hotel.breakfast_type'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)


class AsHotelAmenities(models.Model):
    _name = 'as.hotel.amenities'
    _description = 'as.hotel.amenities'

    name = fields.Char(string='Name', required=True)
    fa_class = fields.Char(string='Font Awesome class')
    description = fields.Text(string='Description')


class AsHotelFacility(models.Model):
    _name = 'as.hotel.facility'
    _description = 'as.hotel.facility'

    name = fields.Char(string='Name', required=True)
    parent_id = fields.Many2one('as.hotel.facility', string='Parent')
    hotel_id = fields.Many2one('as.hotel', string='Hotel', required=True)
    fa_class = fields.Char(string='Font Awesome class')
    description = fields.Text(string='Description')
    type = fields.Selection([
        ('hotel', 'Hotel'),
        ('room', 'Room')
    ], string='Type')


class AsHotelService(models.Model):
    _name = 'as.hotel.service'
    _description = 'as.hotel.service'

    name = fields.Char(string='Name', required=True)
    hotel_id = fields.Many2one('as.hotel', string='Hotel', required=True)
    description = fields.Text(string='Description')
    fa_class = fields.Char(string='Font Awesome class')


class AsHotelPolicy(models.Model):
    _name = 'as.hotel.policy'
    _description = 'as.hotel.policy'

    # section_name = fields.Char(string='Section Name', required=True)
    # section_fa_class = fields.Char(string='Section FA Class')

    section = fields.Selection([
        ('child_and_beds', 'Child & Beds'),
        ('others', 'Others'),
    ])

    name = fields.Char(string='Name', required=True)
    fa_class = fields.Char(string='Font Awesome Class')
    parent_id = fields.Many2one('as.hotel.policy', string='Parent')
    parent_fa_class = fields.Char(string='Parent FA Class')

    hotel_id = fields.Many2one('as.hotel', string='Hotel', required=True)


class AsHotelPaymentMethods(models.Model):
    _name = 'as.hotel.accept_payment_method'
    _description = 'as.hotel.accept_payment_method'

    name = fields.Char(string='Name', required=True)
    hotel_id = fields.Many2one('as.hotel', string='Hotel', required=True)
    image_1920 = fields.Image(string='Image')
    image_1024 = fields.Image("Image 1024", related="image_1920", max_width=1024, max_height=1024, store=True)
    image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512, store=True)
    image_256 = fields.Image("Image 256", related="image_1920", max_width=256, max_height=256, store=True)
    image_128 = fields.Image("Image 128", related="image_1920", max_width=128, max_height=128, store=True)
    code = fields.Char(string='Code')


class AsHotelReview(models.Model):
    _name = 'as.hotel.review'
    _description = 'as.hotel.review'
    _rec_name = 'partner_id'

    hotel_id = fields.Many2one('as.hotel', string='Hotel', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    date = fields.Date(default=lambda self: fields.Date.today(), string='Date')
    star = fields.Selection([
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
    ], string='Star', required=True)
    review = fields.Text(string='Review', required=True)
    images = fields.Many2many('as.image', string='Images')

    def get_review_count(self, hotel_id=None):
        if hotel_id:
            review_records = self.env['as.hotel.review'].sudo().search([('hotel_id', '=', hotel_id)])
            return len(review_records)
        else:
            return 0


class HotelCancellationPolicy(models.Model):
    _name = 'as.hotel.cancellation_policy'
    _description = 'as.hotel.cancellation_policy'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    hotel_id = fields.Many2one('as.hotel', string='Hotel', required=True)
    type = fields.Selection([
        ('refund', 'Refund')
    ])
    description = fields.Text(string='Description')
    code = fields.Char()
    checked = fields.Boolean()
    refund_before_number = fields.Integer(string='Refund Before Num.')
    refund_amount = fields.Integer()
    free_cancellation = fields.Boolean()

    @api.onchange('checked')
    def onchange_checked(self):
        print('onchange checked')
        all_records = self.env['as.hotel.cancellation_policy'].sudo().search([
            ('hotel_id', '=', self.hotel_id.id)
        ])
        # print('self._origin.id', self._origin.id)

        for record in all_records:
            if record.checked:
                if not self._origin.id == record.id:
                    print('UserError')
                    raise UserError(_("It not possible to set multiple as default. Please remove from another first"))


class HotelExtra(models.Model):
    _name = 'as.hotel.extra'
    _description = 'as.hotel.extra'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    hotel_id = fields.Many2one('as.hotel', string='Hotel', required=True)
    amount = fields.Float()


class HotelNearby(models.Model):
    _name = 'as.hotel.nearby'
    _description = 'as.hotel.nearby'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    hotel_id = fields.Many2one('as.hotel', string='Hotel', required=True)
    type = fields.Selection([
        ('atm', 'ATM'),
        ('bakery', 'Bakery'),
        ('bank', 'Bank'),
        ('bar', 'Bar'),
        ('book_store', 'Book Store'),
        ('cafe', 'Cafe'),
        ('clothing_store', 'Clothing Store'),
        ('convenience_store', 'Convenience Store'),
        ('department_store', 'Department Store'),
        ('drugstore', 'Drugstore'),
        ('electronics_store', 'Electronics Store'),
        ('hospital', 'Hospital'),
        ('jewelry_store', 'Jewelry Store'),
        ('movie_theater', 'Movie Theater'),
        ('night_club', 'Night Club'),
        ('park', 'Park'),
        ('pharmacy', 'Pharmacy'),
        ('primary_school', 'Primary School'),
        ('restaurant', 'Restaurant'),
        ('secondary_school', 'Secondary School'),
        ('shoe_store', 'Shoe Store'),
        ('shopping_mall', 'Shopping Mall'),
        ('stadium', 'Stadium'),
        ('supermarket', 'Supermarket'),
        ('tourist_attraction', 'Tourist Attraction'),
        ('university', 'University'),
    ])

    distance = fields.Integer()
    distance_unit = fields.Selection([
        ('min', 'Min'),
        ('hour', 'Hour'),
        ('day', 'Day'),
    ])
    mode = fields.Selection([
        ('driving', 'Driving'),
        ('transit', 'Transit'),
        ('walking', 'Walking'),
        ('cycling', 'Cycling'),
        ('flights', 'Flights'),
    ])
    

class ClassName(models.Model):
    _name = 'as.alert'
    _description = 'as.alert'
    _rec_name = 'alert'

    alert = fields.Text(required=True)


"""
*****************************************************
Stay
*****************************************************
"""


class AsStayService(models.Model):
    _name = 'as.stay'
    _description = 'as.stay'

    name = fields.Char()
    description = fields.Text()
    link = fields.Char()
    code = fields.Char()
    stay_item_ids = fields.Many2many('stay.item', string='Stay Items')


class StayItem(models.Model):
    _name = 'stay.item'
    _description = 'stay.item'

    name = fields.Char()
    description = fields.Text()
    link = fields.Char()
    code = fields.Char()

