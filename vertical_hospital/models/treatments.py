# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class HospitalTreatments(models.Model):
    _name = 'hospital.treatments'
    _description = "Hospital Treatments"

    treatment_code = fields.Char(
        'Treatment code'
    )
    name = fields.Char(
        'Name'
    )
    doctor = fields.Char(
        'Doctor'
    )

    @api.constrains('treatment_code')
    def _check_treatment_code(self):
        # Validamos que el dni no contenga la secuencia 026
        for rec in self:
            if rec.treatment_code and '026' in rec.treatment_code:
                raise models.ValidationError('Treatment code can not contain 026')

