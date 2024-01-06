# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.http import request as req
from datetime import date
import datetime
import base64
from werkzeug.utils import redirect

def get_partner_id():
    uid = http.request.env.user.id
    pid = http.request.env['res.users'].sudo().search([('id', '=', uid)]).partner_id.id
    if pid:
        return pid
    else:
        return None


def get_partner_obj():
    uid = http.request.env.user.id
    pid = http.request.env['res.users'].sudo().search([('id', '=', uid)]).partner_id
    if pid:
        return pid
    else:
        return None


class CleaningService(http.Controller):
    @http.route('/cleaning-service/request', type="http", auth='public', website=True)
    def cleaning_service(self, **kw):
        return req.render('as_rental.cleaning_service_request', {})

    @http.route('/cleaning-service/request/status', type="http", auth='public', website=True)
    def cleaning_service_request_status(self, **kw):
        pid = get_partner_id()
        if not pid:
            return redirect('/web/login')

        # process
        vals = kw

        # Validate form
        if vals.get('cs_days'):
            vals['cs_days'] = int(vals.get('cs_days'))

        if vals.get('cs_peoples_count'):
            vals['cs_peoples_count'] = int(vals.get('cs_peoples_count'))

        if not vals.get('cs_start_date'):
            del vals['cs_start_date']

        if not vals.get('cs_end_date'):
            del vals['cs_end_date']

        if vals.get('cs_days'):
            vals['cs_days'] = int(vals.get('cs_days'))

        # Update with new keys
        vals.update({
            'partner_id': pid
        })

        ssr = req.env['as.cleaning_service.request'].sudo().create(vals)

        if ssr:
            msg = {
                'success': 'Your request successfully sent'
            }
            return req.render('as_rental.msg', {'msg': msg})
        else:
            msg = {
                'danger': 'Something went wrong'
            }
            return req.render('as_rental.msg', {'msg': msg})
