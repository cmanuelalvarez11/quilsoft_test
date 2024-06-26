# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    endpoint = fields.Char(
        string="Endpoint",
        config_parameter="vertical_hospital.endpoint",
    )