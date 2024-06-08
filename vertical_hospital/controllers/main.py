# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import json

from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.http import request
from odoo import http

class VerticalHospitalController(http.Controller):

    @http.route('/pacientes/consulta/<string:sequence>', type='http', auth="public",
                methods=['GET', 'POST'],
                website=True)
    def get_patient(self, **kwargs):
        sequence = kwargs.get('sequence', False)
        if sequence:
            # Si viene la secuencia como parametro
            # buscamos el paciente que coincida, ajustamos para solo devolver 1 registro
            patient_id = request.env['hospital.patients'].sudo().search([('sequence', '=', sequence)], limit=1)
            if patient_id:
                return json.dumps({
                    'sequence': patient_id.sequence,
                    'name': patient_id.name,
                    'dni': patient_id.dni,
                    'state': patient_id.state
                })
            else:
                return json.dumps({})
