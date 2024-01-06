# -*- coding: utf-8 -*-

from odoo import models, fields, api


class WishList(models.Model):
    _name = 'as.wishlist'
    _description = 'as.wishlist'

    partner_id = fields.Many2one('res.partner', string='Partner')
    product_id = fields.Many2one('product.template', string='Product')
    hotel_id = fields.Many2one('as.hotel', string='Hotel')
    date = fields.Date(default=lambda self: fields.Date.today(), string='Date')

    type = fields.Many2one('as.service', string='Type')
    record_id = fields.Integer(string='Record ID')
