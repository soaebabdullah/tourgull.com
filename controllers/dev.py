from odoo import http
from odoo.http import request
from odoo.http import request as req
from werkzeug.utils import redirect
from datetime import date, time
from odoo.tests.common import Form
from odoo.exceptions import AccessError, UserError, AccessDenied
import requests
import json
import base64
from datetime import date, time, datetime


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


class AvDev(http.Controller):

    @http.route('/dev/sts', type="http", auth='public', csrf=False)
    def set_test_session(self, **kw):
        req.session['sts'] = 'success'
        return 'sts'

    @http.route('/dev/gts', type="http", auth='public', csrf=False)
    def get_test_session(self, **kw):
        gts = req.session.get('sts')
        print('gts', gts)
        return f'gts: {gts}'
