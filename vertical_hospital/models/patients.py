# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class HospitalPatients(models.Model):
    _name = 'hospital.patients'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patients"

    sequence = fields.Char(
        'Sequence',
        default='/',
        readonly=True
    )
    name = fields.Char(
        'Name and last name'
    )
    dni = fields.Char(
        'DNI',
        track_visibility='onchange'
    )
    date = fields.Datetime(
        'Date',
        default=fields.Datetime.now
    )
    update_datetime = fields.Datetime(
        'Update datetime',
        default=fields.Datetime.now
    )
    state = fields.Selection(
        [('draft', 'Draft'),
         ('high', 'High'),
         ('low', 'Low')],
        'Status',
        default='draft',
        track_visibility='onchange'
    )
    treatment_ids = fields.Many2many(
        'hospital.treatments'
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['sequence'] = self.env['ir.sequence'].next_by_code('patients_seq')
        return super(HospitalPatients, self).create(vals)

    def write(self, values):
        # Actualizamos la fecha de actualizacion
        values['update_datetime'] = fields.Datetime.now()
        return super(HospitalPatients, self).write(values)

    @api.constrains('dni')
    def _check_dni(self):
        # Validamos que el dni solo contenga digitos
        for rec in self:
            if rec.dni:
                if not rec.dni.isnumeric():
                    raise models.ValidationError('DNI can not contain letters')
