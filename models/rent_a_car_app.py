# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CarApp(models.Model):
    _name = 'rent.car.app'
    _description = 'rent.car.app'

    app_id = fields.Char(compute="_compute_app_id")
    owners_name = fields.Char("Owners Name")
    product = fields.Many2one('product.template', string='Product')
    partner_id = fields.Many2one('res.partner', string='Customer')

    @api.depends('app_id')
    def _compute_app_id(self):
        for record in self:
            record.app_id = 'RENT/CAR/APP/' + str(record.id)


class CarBook(models.Model):
    _name = 'rent.car.book'
    _description = 'rent.car.book'

    partner_id = fields.Many2one('res.partner', string='Customer')
    product = fields.Many2one('product.template', string='Product')
    date = fields.Date(default=lambda self: fields.Date.today(), string='Date')
    paid = fields.Boolean(string='Paid')

    def btn_paid(self):
        self.paid = True

    def btn_unpaid(self):
        self.paid = False


class CarBrand(models.Model):
    _name = 'rent.car.brand'
    _description = 'rent.car.brand'
    _rec_name = 'name'

    name = fields.Char(string='Name')


class CarType(models.Model):
    _name = 'rent.car.type'
    _description = 'rent.car.type'
    _rec_name = 'name'

    name = fields.Char(string='Name')


class ServiceLocation(models.Model):
    _name = 'rent.car.service_location'
    _description = 'rent.car.service_location'
    _rec_name = 'name'

    name = fields.Char(string='Name')


class CarModel(models.Model):
    _name = 'rent.car.model'
    _description = 'rent.car.model'
    _rec_name = 'name'

    name = fields.Char(string='Name')


class ModelYear(models.Model):
    _name = 'rent.car.model_year'
    _description = 'rent.car.model_year'
    _rec_name = 'year'

    year = fields.Char(string='Year')


class RegYear(models.Model):
    _name = 'rent.car.reg_year'
    _description = 'rent.car.reg_year'
    _rec_name = 'year'

    year = fields.Char(string='Year')


class CarPackage(models.Model):
    _name = 'rent.car.package'
    _description = 'rent.car.package'
    _rec_name = 'name'

    name = fields.Char(string='Name')
    valid_name = fields.Char(string='Valid Name', compute="_compute_valid_name", store=True)
    pkg_image = fields.Image(string='Package Image')

    @api.depends('name')
    def _compute_valid_name(self):
        if self.name:
            name = self.name
            a = name.lower()
            b = a.replace(' ', '_')
            self.valid_name = b


class CarSetting(models.Model):
    _name = 'rent.car.slider'
    _description = 'rent.car.slider'
    _rec_name = 'image'

    image = fields.Image(string='Slider Image')
