from odoo import models, fields, api


class AsWebsiteMenu(models.Model):
    _name = 'as.website_menu'
    _description = 'as.website_menu'
    _order = 'sequence'

    name = fields.Char(string='Name')
    url = fields.Char(string='Url')
    parent_id = fields.Many2one('as.website_menu', string='Parent')
    icon_class = fields.Char(string='Icon Class')
    new_window = fields.Boolean(string='New Window')
    sequence = fields.Integer(string='Sequence')
