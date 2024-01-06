# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AsNotification(models.Model):
    _name = 'as.notification'
    _description = 'as.notification'
    _order = 'id desc'

    partner_id = fields.Many2one('res.partner', 'Partner')
    notification = fields.Text(string='Notification')
    url = fields.Char(string='Url')
    seen = fields.Boolean(string='Seen')
    # Below for later
    partner_type = fields.Selection([
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('all', 'All')
    ], default='all', string='Partner Type')
    title = fields.Char(string='Title')
    datetime = fields.Datetime(string='DateTime', default=fields.Datetime.now)


class AsNotificationSeen(models.Model):
    _name = 'as.notification.seen'
    _description = 'as.notification.seen'

    notification_id = fields.Many2one('as.notification', 'Notification')
    partner_id = fields.Many2one('res.partner', 'Partner')
