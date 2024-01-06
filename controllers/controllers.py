# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.http import request as req
from datetime import date
import datetime
import base64
from odoo.addons.http_routing.models.ir_http import slug
from werkzeug.utils import redirect


class AsControllers(http.Controller):
    @http.route('/contact', type="http", auth='public', website=True)
    def contact(self, **kw):
        setting = req.env['as.setting'].sudo().search([], limit=1)
        return req.render('as_rental.contact', {
            'setting': setting,
        })
