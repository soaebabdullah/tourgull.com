from odoo import models, fields, api


class AsResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    rp_temp_book_time = fields.Integer(string='Temporary booking time', default=120)
    rp_av_commission = fields.Integer(string='Av commission (%)', default=15)

    def set_values(self):
        res = super(AsResConfigSettings, self).set_values()

        # custom values
        self.env['ir.config_parameter'].set_param('as_rental.rp_temp_book_time', self.rp_temp_book_time)
        self.env['ir.config_parameter'].set_param('as_rental.rp_av_commission', self.rp_av_commission)

    @api.model
    def get_values(self):
        res = super(AsResConfigSettings, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()

        # Custom values
        tmp_time = ICPSudo.get_param('as_rental.rp_temp_book_time')
        av_commission = ICPSudo.get_param('as_rental.rp_av_commission')
        res.update(
            rp_temp_book_time=int(tmp_time)
        )
        res.update(
            rp_av_commission=int(av_commission)
        )
        return res






