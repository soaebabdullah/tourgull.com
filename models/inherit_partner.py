# remove emergency_phone2, gender2 before final deploy
from odoo import models, fields, api


class InheritPartner(models.Model):
    _inherit = 'res.partner'

    # common
    welcome = fields.Boolean(string='Welcome')
    invite_code = fields.Char(string='Invite Code')
    setting_notification = fields.Boolean(string='Notification')
    setting_message = fields.Boolean(string='Message')
    payment_token = fields.Char(string='Payment Token')

    is_host = fields.Boolean(string='Host (Mode)')
    is_host_approved = fields.Boolean(string='Host Approved')
    document_ok = fields.Boolean(string='Document Ok', help='Partner provided all document and ready to take service like booking')
    commission = fields.Integer(string='As. Commission (%)')

    # new
    emergency_phone = fields.Char(string='Emergency Phone')
    emergency_phone2 = fields.Char(string='Emergency Phone')
    others_phone = fields.Char(string='Others Phone')
    street_permanent = fields.Char(string='Street Permanent')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    gender2 = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender')
    fathers_name = fields.Char(string='Father\'s Name')
    mothers_name = fields.Char(string='Mother\'s Name')
    date_of_birth = fields.Date(string='Date Of Birth')
    nid_passport_no = fields.Char(string='NID/Passport No')
    nid_passport_front = fields.Binary(string='NID/Passport Front')
    nid_passport_back = fields.Binary(string='NID/Passport Back')
    company_name = fields.Char(string='Company Name')
    middle_name = fields.Char(string='Middle Name')
    last_name = fields.Char(string='Last Name')
    apt = fields.Char(string='Apt./Suite/Others')
    state = fields.Char(string='District/State')

    # NID
    nid_number = fields.Char(string='NID Number')
    nid_front_1920 = fields.Image(string='NID Front', max_width=1920, max_height=1920)
    nid_front_1024 = fields.Image("Image 1024", related="nid_front_1920", max_width=1024, max_height=1024, store=True)
    nid_front_512 = fields.Image("Image 512", related="nid_front_1920", max_width=512, max_height=512, store=True)
    nid_front_256 = fields.Image("Image 256", related="nid_front_1920", max_width=256, max_height=256, store=True)
    nid_front_128 = fields.Image("Image 128", related="nid_front_1920", max_width=128, max_height=128, store=True)
    nid_back_1920 = fields.Image(string='NID Back', max_width=1920, max_height=1920)
    nid_back_1024 = fields.Image("Image 1024", related="nid_back_1920", max_width=1024, max_height=1024, store=True)
    nid_back_512 = fields.Image("Image 512", related="nid_back_1920", max_width=512, max_height=512, store=True)
    nid_back_256 = fields.Image("Image 256", related="nid_back_1920", max_width=256, max_height=256, store=True)
    nid_back_128 = fields.Image("Image 128", related="nid_back_1920", max_width=128, max_height=128, store=True)

    # Passport
    passport_number = fields.Char(string='Passport Number')
    passport_photo_page_1920 = fields.Image(string='Passport Photo Page', max_width=1920, max_height=1920)
    passport_photo_page_1024 = fields.Image("Image 1024", related="passport_photo_page_1920", max_width=1024, max_height=1024, store=True)
    passport_photo_page_512 = fields.Image("Image 512", related="passport_photo_page_1920", max_width=512, max_height=512, store=True)
    passport_photo_page_256 = fields.Image("Image 256", related="passport_photo_page_1920", max_width=256, max_height=256, store=True)
    passport_photo_page_128 = fields.Image("Image 128", related="passport_photo_page_1920", max_width=128, max_height=128, store=True)
    passport_contact_page_1920 = fields.Image(string='Passport Contact Page', max_width=1920, max_height=1920)
    passport_contact_page_1024 = fields.Image("Image 1024", related="passport_contact_page_1920", max_width=1024, max_height=1024, store=True)
    passport_contact_page_512 = fields.Image("Image 512", related="passport_contact_page_1920", max_width=512, max_height=512, store=True)
    passport_contact_page_256 = fields.Image("Image 256", related="passport_contact_page_1920", max_width=256, max_height=256, store=True)
    passport_contact_page_128 = fields.Image("Image 128", related="passport_contact_page_1920", max_width=128, max_height=128, store=True)

    # Present address
    pre_country_id = fields.Many2one('res.country', string='Country')
    pre_street = fields.Char(string='Street Address')
    pre_apt = fields.Char(string='Apt./Suite/Others')
    pre_city = fields.Char(string='Thana/City')
    pre_state = fields.Char(string='District/State')
    pre_zip = fields.Char(string='Zip Code')

    # tour guide
    tg_is_tour_guide = fields.Boolean(string='Tour guide')
    tg_about_me = fields.Text(string='About me')
    tg_description = fields.Text(string='Description')
    tg_tours = fields.Integer(string='Tours', default=0)
    tg_views = fields.Integer(string='Views', default=0)
    tg_lang = fields.Many2many('res.lang', string='Languages')
    tg_hourly_rate = fields.Integer(string='Hourly rate', default=0)
    tg_review = fields.Many2many('as.tour_guide.review', string='Review')
    tg_place = fields.Many2many('as.tour_guide.place', string='Places')

    # Business Profile
    bp_business_name = fields.Char(string='Business Name')
    bp_tl_name = fields.Char(string='TL Name')
    bp_business_category = fields.Char(string='Business Category')
    bp_street = fields.Text(string='Address')
    bp_mobile = fields.Char(string='Mobile')
    bp_email = fields.Char(string='Email')

    """
    bp_business_name
    bp_tl_name
    bp_business_category
    bp_street
    bp_mobile
    bp_email
    """
