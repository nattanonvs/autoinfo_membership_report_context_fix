from odoo import fields, models

from .. import hooks


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    autoinfo_membership_report_context_fix_enabled = fields.Boolean(
        string="Enable Membership Report Context Fix",
        config_parameter=hooks.PARAM_ENABLED,
        default=True,
    )

    def set_values(self):
        res = super().set_values()
        hooks.apply_fix(self.env)
        return res

