from odoo import models, fields, api


# def get_partner_id():
#     uid = http.request.env.user.id
#     partner_id = http.request.env['res.users'].sudo().search([('id', '=', uid)]).partner_id.id
#     if partner_id:
#         return partner_id
#     else:
#         return None
#
#
# def get_partner_obj():
#     uid = self.env.context.get('uid')
#     partner_obj = http.request.env['res.users'].sudo().search([('id', '=', uid)]).partner_id
#     if partner_obj:
#         return partner_obj
#     else:
#         return None

class AsDef(models.Model):
    _name = 'as.def'
    _description = 'as.def'

    name = fields.Char(string='Name')

    def switch_user(self):
        uid = self.env.user.id

        if not uid:
            return

        pt = self.env['res.users'].sudo().search([('id', '=', uid)]).partner_id

        if not pt:
            return

        pid = pt.id

        if not pid:
            return

        if pt.is_host:
            if pt.partner_type == 'rp_host':
                # switch to personal
                return 'switch_to_personal'
            else:
                # Switch to host
                return 'switch_to_host'
        else:
            return False

    def get_navs(self):
        menu_level_0 = self.env['as.website_menu'].sudo().search([('parent_id', '=', 4)])
        for menu in menu_level_0:
            menu_level_1 = self.env['as.website_menu'].sudo().search([('parent_id', '=', menu.id)])
            print(menu.name)
            for sub_menu in menu_level_1:
                print(f'---{sub_menu.name}')
            print('---------')

    def get_partner_obj(self):
        uid = self.env.user.id
        pid = self.env['res.users'].sudo().search([('id', '=', uid)]).partner_id
        if pid:
            return pid
        else:
            return None

    def get_wishlist_count(self):
        pt = self.get_partner_obj()
        if pt:
            ws = self.env['as.wishlist'].sudo().search([('partner_id', '=', pt.id)])
            ws_count = len(ws)
            return ws_count
        else:
            return False

    def get_notification_count(self):

        pt = self.get_partner_obj()

        # Get partner type wise records
        pt_type_recs = None
        if pt.is_host:
            pt_type_recs = self.env['as.notification'].sudo().search([('partner_type', '=', 'host')])
        else:
            pt_type_recs = self.env['as.notification'].sudo().search([('partner_type', '=', 'guest')])

        # Get all type records
        all_type_recs = self.env['as.notification'].sudo().search([('partner_type', '=', 'all')])

        # Get partner wise records
        pt_recs = self.env['as.notification'].sudo().search([('partner_id', '=', pt.id)])

        # Merge records
        notifications = pt_type_recs + all_type_recs + pt_recs
        nf_len = len(notifications)
        return nf_len

    def get_message_count(self):
        pt = self.get_partner_obj()

        # Get partner messages count
        pt_recs = self.env['as.message'].sudo().search([('partner_id', '=', pt.id)])

        msg_len = len(pt_recs)
        return msg_len

    def as_visit(self, full_path):
        pt = self.get_partner_obj()
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        full_url = f'{base_url}{full_path}'

        vals = {
            'url': full_url,
        }

        if pt:
            vals['partner_id'] = pt.id

        visit = self.env['as.visit'].sudo().create(vals)

    # def get_all_notifications(self):
    #     pt = self.get_partner_obj()
    #     if not pt:
    #         return False
    #
    #     # Get partner type wise records
    #     pt_type_notifications = None
    #     if pt.is_host:
    #         pt_type_notifications = self.env['as.notification'].sudo().search([('partner_type', '=', 'host')])
    #         print('is_host')
    #
    #     if not pt.is_host:
    #         pt_type_notifications = self.env['as.notification'].sudo().search([('partner_type', '=', 'guest')])
    #         print('not is_host')
    #
    #     # Get all type records
    #     all_type_notifications = self.env['as.notification'].sudo().search([('partner_type', '=', 'all')])
    #
    #     # Get partner wise records
    #     pt_notifications = self.env['as.notification'].sudo().search([('partner_id', '=', pt.id)])
    #
    #     # Merge all records
    #     notifications = pt_type_notifications + all_type_notifications + pt_notifications
    #     notifications.aaa = '_aaa_'
    #     print('notifications', notifications)
    #     print('notifications', notifications.aaa)
    #
    #     # Check seen
    #     nts = []
    #     seen = self.env['as.notification.seen'].sudo().search([('partner_id', '=', pt.id)])
    #     for notification in notifications:
    #         seen_notification = self.env['as.notification.seen'].sudo().search([
    #             ('notification_id', '=', notification.id),
    #             ('partner_id', '=', pt.id),
    #         ], limit=1)
    #         if not seen_notification:
    #             notification.seen = True
    #             nts.append(notification)
    #
    #     print('nts', nts)
    #     return nts

    def get_all_notifications(self):
        pt = self.get_partner_obj()
        if not pt:
            return False

        nts = self.env['as.notification'].sudo().search([('partner_id', '=', pt.id)], limit=20)
        nts_unseen_count = self.env['as.notification'].sudo().search_count([
            ('partner_id', '=', pt.id),
            ('seen', '=', False),
        ])
        nt_dict = {
            'nts': nts,
            'nts_unseen_count': nts_unseen_count,
        }
        # print('nts', nts)
        # print('nts_unseen_count', nts_unseen_count)
        return nt_dict
