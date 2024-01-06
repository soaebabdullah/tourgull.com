# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TourGuideReview(models.Model):
    _name = 'as.tour_guide.review'
    _description = 'as.tour_guide.review'

    name = fields.Text(string='Name')


class TourGuidePlace(models.Model):
    _name = 'as.tour_guide.place'
    _description = 'as.tour_guide.place'

    name = fields.Text(string='Name')


class TourGuideHire(models.Model):
    _name = 'as.tour_guide.hire'
    _description = 'as.tour_guide.hire'

    partner_id = fields.Many2one('res.partner', string='Partner')
    date = fields.Date(default=lambda self: fields.Date.today(), string='Date')
    guide_id = fields.Many2one('res.partner', string='Guide')
