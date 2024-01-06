# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime


class HostApp(models.Model):
    _name = 'host.app'
    _description = 'host.app'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', string='Partner', tracking=True)
    status = fields.Selection([('pending', 'Pending'), ('approved', 'Approved'), ], 'Status', default='pending')

    def approve(self):
        # self.partner_id.is_host = True
        self.partner_id.is_host_approved = True
        self.status = 'approved'

    def pending(self):
        # self.partner_id.is_host = False
        self.partner_id.is_host_approved = False
        self.status = 'pending'


# List property request
class RentHostApp(models.Model):
    _name = 'rent.host.app'
    _description = 'rent.host.app'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'partner_id'

    partner_id = fields.Many2one('res.partner', string='Customer')
    product_id = fields.Many2one('product.template', string='Product')
    rp_is_host_prop = fields.Boolean(string='Publish', related='product_id.rp_is_host_prop', readonly=True, tracking=True)

    def publish(self):
        if self.product_id:
            self.product_id.rp_is_host_prop = True

    def un_publish(self):
        if self.product_id:
            self.product_id.rp_is_host_prop = False


class HostPropertyType(models.Model):
    _name = 'host.property_type'
    _description = 'host.property_type'
    _rec_name = 'name'

    name = fields.Char()


class HostPlaceType(models.Model):
    _name = 'host.place_type'
    _description = 'host.place_type'
    _rec_name = 'name'

    name = fields.Char()


class HostAme1(models.Model):
    _name = 'host.ame_1'
    _description = 'host.ame_1'
    _rec_name = 'name'
    _order = 'sequence,id'

    sequence = fields.Integer(default=10, string='Sequence')
    name = fields.Char()


class HostAme2(models.Model):
    _name = 'host.ame_2'
    _description = 'host.ame_2'
    _rec_name = 'name'

    name = fields.Char()


class HostAme3(models.Model):
    _name = 'host.ame_3'
    _description = 'host.ame_3'
    _rec_name = 'name'

    name = fields.Char()


class rentPropertyBook(models.Model):
    _name = 'rent.property.book'
    _description = 'rent.property.book'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'product'

    partner_id = fields.Many2one('res.partner', string='Partner')
    product = fields.Many2one('product.template', string='Product')
    date = fields.Date(default=lambda self: fields.Date.today(), string='Date')
    # paid = fields.Boolean(string='Paid')
    quotation = fields.Boolean(string='Qt. Status')
    quot_rel = fields.Many2one('sale.order', string='Sale Order')
    check_in = fields.Date(string='CheckIn')
    check_out = fields.Date(string='CheckOut')
    rp_is_book = fields.Boolean(string='Book', related='product.rp_is_book', readonly=False)
    host_id = fields.Many2one(string='Host', related='product.rp_host', readonly=False)
    book_confirm = fields.Boolean(string='Book Confirm')
    review_state = fields.Selection([
        ('available', 'Available'),
        ('done', 'done'),
    ], string='Review State')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
    ], string='State', default='draft', tracking=True)

    @api.model
    def cron_auto_checkout(self):
        print('cron_auto_checkout')
        bookings = self.env['rent.property.book'].sudo().search([])
        date_today = date.today()

        for booking in bookings:
            if booking.state == 'confirm' and booking.check_out < date_today:
                booking.state = 'done'
                booking.rp_is_book = False
                print(f'{booking} has been checkout')

    @api.onchange('rp_is_book')
    def calculate_review_available(self):
        print('call: review_available')
        if self.rp_is_book:
            self.review_state = 'available'
            print('review_state: available')

    def create_sale_order(self):
        pd_id = self.env['product.product'].sudo().search([('product_tmpl_id', '=', self.product.id)]).id
        print('pd_id', pd_id)
        so = self.env['sale.order'].sudo().create({
            'partner_id': self.partner_id.id,
            'order_line': [
                (0, 0, {
                    'product_id': pd_id,
                    'product_uom_qty': 1.0,
                    'tax_id': False,
                })],
        })

        if so:
            # self.quotation = True
            self.quot_rel = so.id
            print('so', so)

    def confirm_booking(self):
        self.book_confirm = True
        self.rp_is_book = True
        self.state = 'confirm'

        if self.product:
            self.product.rp_book_temp_datetime = None

        if not self.review_state:
            self.review_state = 'available'

        # SMS/Email will send to confirm

    def cancel_booking(self):
        self.rp_is_book = False
        self.state = 'done'

    def set_to_draft(self):
        self.state = 'draft'
        self.book_confirm = False
        self.review_state = None


class PropSliders(models.Model):
    _name = 'rent.property.slider'
    _description = 'rent.property.slider'
    _rec_name = 'image'

    image = fields.Image(string='Slider')


class RentPropertyReview(models.Model):
    _name = 'rent.property.review'
    _description = 'rent.property.review'
    _rec_name = 'partner_id'

    product_id = fields.Many2one('product.template', string='Product', required=True)
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

    def get_review_count(self, pd_id=None):
        if pd_id:
            review_records = self.env['rent.property.review'].sudo().search([('product_id', '=', pd_id)])
            return len(review_records)
        else:
            return 0


class ServiceCategories(models.Model):
    _name = 'as.service.category'
    _description = 'as.service.category'
    _rec_name = 'name'
    _order = 'sequence,id'

    sequence = fields.Integer(string='Sequence')
    name = fields.Char(string='Category Name', required=True)
    parent_id = fields.Many2one('as.service.category', string='Parent Category')
    url = fields.Char(string='Url')
    code = fields.Char(string='Code')
    fa_class = fields.Char(string='Font awesome')
