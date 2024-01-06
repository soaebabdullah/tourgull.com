# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SecurityService(models.Model):
    _name = 'as.security_service.request'
    _description = 'as.security_service.request'
    _order = 'id desc'

    partner_id = fields.Many2one('res.partner', string='Partner')
    date = fields.Date(default=lambda self: fields.Date.today(), string='Date')
    ss_name = fields.Char(string='Your Name')
    ss_address = fields.Text(string='Your Address')

    ss_service_address = fields.Text(string='Service Address')
    ss_days = fields.Integer(string='Total Days')
    ss_peoples_count = fields.Integer(string='Peoples Count')
    ss_start_date = fields.Date(string='Start Date')
    ss_end_date = fields.Date(string='End Date')
