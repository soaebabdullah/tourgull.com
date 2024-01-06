# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AsVisit(models.Model):
    _name = 'as.visit'
    _description = 'as.visit'

    url = fields.Char(string='Url')
    partner_id = fields.Many2one('res.partner', string='Partner')
    datetime = fields.Datetime(string='DateTime', default=fields.Datetime.now)
