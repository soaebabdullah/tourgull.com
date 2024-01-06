# -*- coding utf-8 -*-

from odoo import models, fields, api
from odoo.addons.http_routing.models.ir_http import slug
from datetime import datetime


class InheritProduct(models.Model):
    _inherit = 'product.template'

    """
    '''
    --------------------------------------------------------------
    ------------------- Rent A Car Fields----------------------
    --------------------------------------------------------------
    '''
    # is_rent_car = fields.Boolean()
    # rent_car_type = fields.Char()
    # rent_car_service_location = fields.Char()

    # Technical
    rc_is_rent_car = fields.Boolean(string="Is Rent A Car")
    rc_book_price = fields.Float(string='Booking Price')
    rc_comm_percentage = fields.Integer(string='Commission (%)', default=15)
    rc_exp_date = fields.Date(string="Expired Date")
    rc_pkg = fields.Many2one('rent.car.package', string="Package")

    # Owner's Description
    rc_owner_s_name = fields.Char(string="Owner's Name")
    rc_company_name = fields.Char(string="Company Name")
    rc_address = fields.Char(string="Address")
    rc_city = fields.Char(string="City")
    rc_mobile = fields.Char(string="Mobile")
    rc_email = fields.Char(string="Email")

    # Driver's Information
    rc_dr_name = fields.Char(string="Driver Name")
    rc_dr_father_name = fields.Char(string="Father's Name")
    rc_dr_mother_name = fields.Char(string="Mother's Name")
    rc_dr_dof = fields.Date(string="Date Of Birth")
    rc_dr_gender = fields.Selection([('male', 'Male'), ('female', 'Female')], default='male', string='Gender')
    rc_dr_marital_status = fields.Char(string="Marital status")
    rc_dr_nid_no = fields.Char(string="NID No")
    rc_dr_nid_image_front = fields.Image(string="NID Image Front")
    rc_dr_nid_image_back = fields.Image(string="NID Image Back")

    # Car's description
    rc_title = fields.Char(string="Title")
    rc_brand_name = fields.Many2one('rent.car.brand', string="Brand Name")
    rc_car_type = fields.Many2one('rent.car.type', string="Car Type")
    rc_service_location = fields.Many2one('rent.car.service_location', string="Service Location")
    # short_desc
    # long_desc
    rc_model = fields.Char(string="Model")
    rc_model_year = fields.Many2one('rent.car.model_year', string="Model Year")
    rc_cng = fields.Selection([('yes', 'Yes'), ('no', 'No'), ], 'CNG', default='no')
    rc_reg_year = fields.Many2one('rent.car.reg_year', string="Registration Year")
    rc_reg_number = fields.Char(string="Registration Number")
    rc_cars_garage_location = fields.Char(string="Garage Location")

    # Images
    rc_fitness_certificate = fields.Image(string="Fitness Certificate")
    rc_reg_certificate = fields.Image(string="Registration Certificate")
    rc_tax_token = fields.Char(string="Tax Token")

    @api.onchange('rc_book_price')
    def _make_list_price(self):
        if self.rc_book_price:
            a = self.rc_book_price / 100
            b = a * self.rc_comm_percentage
            self.list_price = self.rc_book_price + b
    
    """

    '''
    --------------------------------------------------------------
    ------------------- Host Property Fields----------------------
    --------------------------------------------------------------
    '''
    # Technical
    rp_is_host_prop = fields.Boolean(string='Rental Place')
    rp_hotel = fields.Many2one('as.hotel', string='Hotel')
    rp_is_book = fields.Boolean(string='Book')
    # rp_is_temp_book = fields.Boolean(string='Book (temp)')
    # rp_temp_book_time = fields.Boolean(string='Book time (sec)')
    rp_book_temp_time = fields.Char(string='Book time (sec)')
    rp_book_temp_datetime = fields.Datetime(string='Book Temp Datetime')
    rp_host = fields.Many2one('res.partner', string='Host')
    rp_start_date = fields.Date(default=lambda self: fields.Date.today(), string='Start Date')
    rp_end_date = fields.Date(default=lambda self: datetime.strptime('2050/01/01', '%Y/%m/%d'), string='End Date')

    # @api.depends('rp_end_date')
    # def _compute_rp_end_date(self):
    #     #     date_future_str = '01/01/2050'
    #     #     date_future_obj = datetime.strptime(date_future_str, '%d/%m/%Y')
    #     #     self.rp_end_date = date_future_obj
    #     if not self.rp_end_date:
    #         print('None found')

    rp_state = fields.Selection([
        ('arriving', 'Arriving'),
        ('hosting', 'Hosting'),
        ('checking_out', 'Checking Out'),
    ], default='arriving', string='Hosting state')

    # Property
    rp_pro_type = fields.Many2one('host.property_type', string='Property Type')
    rp_place_type = fields.Many2one('host.place_type', string='Place Type')

    # Location
    rp_lat = fields.Char(string='Latitude')
    rp_lng = fields.Char(string='Longitude')

    rp_country = fields.Many2one('res.country', string='Country')
    rp_address = fields.Char(string='Street Address')
    rp_apt = fields.Char(string='Apt./Suite/Others')
    rp_city = fields.Char(string='Thana/City')
    rp_district_state = fields.Char(string='District/State')
    rp_zip = fields.Char(string='ZIP Code')

    rp_contact_person = fields.Char(string='Contact Person')
    rp_contact_phone = fields.Char(string='Contact Phone')

    # Description
    rp_guests = fields.Integer(string='Guests')
    rp_adults = fields.Integer(string='Adults')
    rp_childs = fields.Integer(string='Childs')
    rp_beds = fields.Integer(string='Beds')
    rp_king_beds = fields.Integer(string='King beds')
    rp_bedrooms = fields.Integer(string='Bedrooms')
    rp_bathrooms = fields.Integer(string='Bathrooms')
    rp_is_bath_private = fields.Selection([('yes', 'Yes'), ('no', 'No')], string='Is Bathroom Private?')

    # Amenities
    rp_amenities_1 = fields.Many2many('host.ame_1', string='Amenities')
    rp_amenities_2 = fields.Many2many('host.ame_2', string='Amenities 2')
    rp_amenities_3 = fields.Many2many('host.ame_3', string='Amenities 3')

    # Title
    rp_place_name = fields.Char(string='Place Name')
    rp_place_desc = fields.Text(string='Place Description')

    # Price
    rp_price = fields.Float(string='Price')

    # Media - Images
    rp_image_2 = fields.Image(string='Image 02')
    rp_image_3 = fields.Image(string='Image 03')
    rp_image_4 = fields.Image(string='Image 04')
    rp_image_5 = fields.Image(string='Image 05')

    rp_image_2_1024 = fields.Image("Image 1024", related="rp_image_2", max_width=1024, max_height=1024, store=True)
    rp_image_2_512 = fields.Image("Image 512", related="rp_image_2", max_width=512, max_height=512, store=True)
    rp_image_2_256 = fields.Image("Image 256", related="rp_image_2", max_width=256, max_height=256, store=True)
    rp_image_2_128 = fields.Image("Image 128", related="rp_image_2", max_width=128, max_height=128, store=True)

    rp_image_3_1024 = fields.Image("Image 1024", related="rp_image_3", max_width=1024, max_height=1024, store=True)
    rp_image_3_512 = fields.Image("Image 512", related="rp_image_3", max_width=512, max_height=512, store=True)
    rp_image_3_256 = fields.Image("Image 256", related="rp_image_3", max_width=256, max_height=256, store=True)
    rp_image_3_128 = fields.Image("Image 128", related="rp_image_3", max_width=128, max_height=128, store=True)

    rp_image_4_1024 = fields.Image("Image 1024", related="rp_image_4", max_width=1024, max_height=1024, store=True)
    rp_image_4_512 = fields.Image("Image 512", related="rp_image_4", max_width=512, max_height=512, store=True)
    rp_image_4_256 = fields.Image("Image 256", related="rp_image_4", max_width=256, max_height=256, store=True)
    rp_image_4_128 = fields.Image("Image 128", related="rp_image_4", max_width=128, max_height=128, store=True)

    rp_image_5_1024 = fields.Image("Image 1024", related="rp_image_5", max_width=1024, max_height=1024, store=True)
    rp_image_5_512 = fields.Image("Image 512", related="rp_image_5", max_width=512, max_height=512, store=True)
    rp_image_5_256 = fields.Image("Image 256", related="rp_image_5", max_width=256, max_height=256, store=True)
    rp_image_5_128 = fields.Image("Image 128", related="rp_image_5", max_width=128, max_height=128, store=True)

    rp_place_categ_id = fields.Many2one('as.place_category', string='Place Category')
    rp_image_ids = fields.Many2many('as.image', string='More Images')
    rp_square_feet = fields.Char(string='Square Feet')

    # Common
    price = fields.Float(string='Price')
    discount = fields.Integer(string='Discount (%)')  # Currently using for hotel room

    # Booleans
    rp_city_view = fields.Boolean(string='City View')

    # Hotel rooms
    available_room = fields.Integer(string='Room Available')

    '''
    --------------------------------------------------------------
    ------------------- Tourist Attraction Fields----------------------
    --------------------------------------------------------------
    '''

    ta_is_ta = fields.Boolean(string='Tourist Attraction')

    # override
    preview_url = fields.Char(string='Preview')
    external_url = fields.Char(string='External Url')

    @api.model
    def create(self, vals):
        res = super(InheritProduct, self).create(vals)
        # print('create working')
        # print('vals_list', vals)
        # print('res', res)
        res.preview_url = f'/shop/product/{slug(res)}'
        return res

    def write(self, vals):
        vals['preview_url'] = f'/shop/product/{slug(self)}'
        result = super(InheritProduct, self).write(vals)
        # print('write working')
        # print('write', self)
        return result
