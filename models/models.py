# all small types of models

from odoo import models, fields, api


class AsMessage(models.Model):
    _name = 'as.message'
    _description = 'as.message'

    partner_id = fields.Many2one('res.partner', 'Partner')
    message = fields.Text(string='Message')
    datetime = fields.Datetime(string='DateTime', default=fields.Datetime.now)


class AsFamily(models.Model):
    _name = 'as.family'
    _description = 'as.family'

    partner_id = fields.Many2one('res.partner', string='Partner')
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    date_of_birth = fields.Date(string='Date Of Birth')
    gender = fields.Selection([
        ('male', "Male"),
        ('female', "Female"),
        ('other', "Other"),
    ], string='Gender')
    image_1920 = fields.Image(string='Photo')
    relationship = fields.Selection([
        ('father', "Father"),
        ('mother', "Mother"),
        ('brother', "Brother"),
        ('sister', "Sister"),
        ('wife', "Wife"),
        ('friend', "Friend"),
        ('other', "Other"),
    ], string='Relationship')
    language = fields.Many2one('res.lang', string='Language')
    parental_responsibility = fields.Boolean(string='Parental Responsibility')
    up_drop = fields.Boolean(string='Up/Drop')
    live_with = fields.Many2one('res.partner', string='Live With')
    notes = fields.Text(string='Notes')


class AsPoint(models.Model):
    _name = 'as.point'
    _description = 'as.point'

    partner_id = fields.Many2one('res.partner', string='Partner')
    point = fields.Integer(string='Point')


class AsPointStore(models.Model):
    _name = 'as.point_store'
    _description = 'as.point_store'

    title = fields.Char(string='title')
    image_1920 = fields.Image(string='Image')
    point = fields.Char(string='point')

    # Image versions
    image_128 = fields.Image("Image 128", related="image_1920", max_width=128, max_height=128, store=True)


class AsGiftCard(models.Model):
    _name = 'as.gift_card'
    _description = 'as.gift_card'

    amount_of_gift_card = fields.Float(string='Amount Of Gift Card')
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    shipping_address = fields.Text(string='Shipping Address')
    shipping_address_2 = fields.Text(string='Shipping Address 2')
    city = fields.Char(string='City')
    region = fields.Char(string='Region')
    zip = fields.Char(string='Zip Code')
    country_id = fields.Many2one('res.country', string='Country')

    pu_first_name = fields.Char(string='First Name')
    pu_last_name = fields.Char(string='Last Name')
    pu_billing_address = fields.Text(string='Shipping Address')
    pu_billing_address_2 = fields.Text(string='Shipping Address 2')
    pu_city = fields.Char(string='City')
    pu_region = fields.Char(string='Region')
    pu_zip = fields.Char(string='Zip Code')
    pu_country_id = fields.Many2one('res.country', string='Country')
    pu_phone = fields.Char(string='Phone')
    pu_email = fields.Char(string='Email')


class AsPaymentMethod(models.Model):
    _name = 'as.payment_acquirer'
    _description = 'as.payment_acquirer'

    name = fields.Char(string='Name', required=True)
    image_1920 = fields.Image(string='Name')
    image_128 = fields.Image(string='Image', related="image_1920", max_width=128, max_height=128)
    secret_id = fields.Char(string='Secret ID')
    secret_password = fields.Char(string='Secret Password')
    code = fields.Char(string='Code', required=True)
    journal_id = fields.Many2one('account.journal', string='Journal')
    method_active = fields.Boolean(string='Active')


class AsSetting(models.Model):
    _name = 'as.setting'
    _description = 'as.setting'

    support_email = fields.Char(string='Support Email')
    support_phone = fields.Char(string='Support Phone')
    currency_symbol = fields.Char(string='Currency Symbol')
    order_temp_time = fields.Integer(string='Order Temp Time (Minute)')
    commission = fields.Integer(string='Commission(%)')


class AsImage(models.Model):
    _name = 'as.image'
    _description = 'as.image'

    image_1920 = fields.Image(string='Image', max_width=1920, max_height=1920, required=True)
    image_1024 = fields.Image("Image 1024", related="image_1920", max_width=1024, max_height=1024, store=True)
    image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512, store=True)
    image_256 = fields.Image("Image 256", related="image_1920", max_width=256, max_height=256, store=True)
    image_128 = fields.Image("Image 128", related="image_1920", max_width=128, max_height=128, store=True)


class AsEventCategory(models.Model):
    _name = 'as.event_category'
    _description = 'as.event_category'
    _order = 'sequence,id'

    sequence = fields.Integer(string='Sequence')
    name = fields.Char(string='Category', required=True)


class AsEventRegistration(models.Model):
    _name = 'as.event_registration'
    _description = 'as.event_registration'

    responsible_id = fields.Many2one('res.partner', string='Responsible')
    name = fields.Char(string='Attendee Name', required=True)
    mobile = fields.Char(string='Mobile', required=True)
    email = fields.Char(string='Email')
    event_id = fields.Many2one('as.event', string='Event')
    # Event Ticket = fields.Many2one('as.event', string='Event')
    registration_date = fields.Date(string='Reg. Date', default=lambda self: fields.Date.today())
    attended_date = fields.Date(string='Attended Date')
    order_id = fields.Many2one('sale.order', ondelete="cascade", string='Sale Order')
    # order_state = fields.Char(related='order_id.state', string='Order State')


class AsEvent(models.Model):
    _name = 'as.event'
    _description = 'as.event'

    name = fields.Char(string='Name', required=True)
    date_start = fields.Date(string='Date Start')
    date_end = fields.Date(string='Date End')
    event_date = fields.Date(string='Event date')
    package = fields.Boolean(string='Package')
    minimum_attendees = fields.Integer(string='Minimum Attendees')
    maximum_attendees = fields.Integer(string='Maximum Attendees')
    event_ticket_ids = fields.Many2many('as.event_registration', string='Attendees')

    event_from = fields.Char(string='Event From')
    destination = fields.Char(string='Destination')

    image_1920 = fields.Image(string='Image')
    image_1024 = fields.Image("Image 1024", related="image_1920", max_width=1024, max_height=1024, store=True)
    image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512, store=True)
    image_256 = fields.Image("Image 256", related="image_1920", max_width=256, max_height=256, store=True)
    image_128 = fields.Image("Image 128", related="image_1920", max_width=128, max_height=128, store=True)
    image_ids = fields.Many2many('as.image', string='Images')

    detail = fields.Html(string='Post Detail')
    published = fields.Boolean(string='Published')
    list_price = fields.Float(string='Price')
    day = fields.Integer(string='Days')
    night = fields.Integer(string='Nights')
    transport = fields.Char(string='Transport')
    category_ids = fields.Many2many('as.event_category', string='Category')

    def btn_publish(self):
        self.published = True

    def btn_un_publish(self):
        self.published = False


class AsPayment(models.Model):
    _name = 'as.payment'
    _description = 'as.payment'

    payment_type = fields.Selection([
        ('inbound', 'Receive Money'),
        ('outbound', 'Send Money'),
        ('transfer', 'Transfer'),
    ], default='inbound', string='Payment type', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    amount = fields.Float(string='Amount', required=True)


class AsCheckingOut(models.Model):
    _name = 'as.checking_out'
    _description = 'as.checking_out'

    product_id = fields.Many2one('product.template', string='Product')
    partner_id = fields.Many2one('res.partner', string='Partner')
    date = fields.Date(string='Date', default=lambda self: fields.Date.today())


class AsPlaceCategory(models.Model):
    _name = 'as.place_category'
    _description = 'as.place_category'
    _order = 'sequence,id'

    sequence = fields.Integer(string='Sequence')
    name = fields.Char(string='Category name', required=True)
    parent_id = fields.Many2one('as.place_category', string='Parent Category')


class AsTodayDeals(models.Model):
    _name = 'as.deal'
    _description = 'as.deal'

    deal = fields.Reference(selection=[
        ('as.event', 'Event'),
        ('product.template', 'Stay'),
    ], string='Deal')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')


class AsTodayDealsEvent(models.Model):
    _name = 'as.deal.event'
    _description = 'as.deal.event'
    _order = 'sequence,id'

    sequence = fields.Integer(string='Sequence')
    event_id = fields.Many2one('as.event', string='Event')


class AsTodayDealsStays(models.Model):
    _name = 'as.deal.stay'
    _description = 'as.deal.stay'
    _order = 'sequence,id'

    sequence = fields.Integer(string='Sequence')
    stay_id = fields.Many2one('product.template', string='Stay')


class AsSearch(models.Model):
    _name = 'as.search'
    _description = 'as.search'
    _rec_name = 'area'
    _order = 'id desc'

    query = fields.Char(string='Query')
    area = fields.Char(string='Area')
    partner_id = fields.Many2one('res.partner', string='Partner')


class FaClass(models.Model):
    _name = 'fa.class'
    _description = 'fa.class'

    name = fields.Char(string='Name', required=True)


class AsServices(models.Model):
    _name = 'as.service'
    _description = 'as.service'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='Code', required=True)

