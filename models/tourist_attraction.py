from odoo import models, fields, api


class SecurityService(models.Model):
    _name = 'as.tourist_attraction'
    _description = 'as.cleaning_service'
    _order = 'id desc'

    ta_name = fields.Char(string='Name')
    # partner_id = fields.Many2one('res.partner', string='Partner')
    # date = fields.Date(default=lambda self: fields.Date.today(), string='Date')
    # cs_name = fields.Char(string='Your Name')
    # cs_address = fields.Text(string='Your Address')
    #
    # cs_service_address = fields.Text(string='Service Address')
    # cs_days = fields.Integer(string='Total Days')
    # cs_peoples_count = fields.Integer(string='Peoples Count')
    # cs_start_date = fields.Date(string='Start Date')
    # cs_end_date = fields.Date(string='End Date')
