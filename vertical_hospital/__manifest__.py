# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': "Vertical Hospital",
    'summary': """
      Functionality for the vertical hospital
    """,
    'description': """
       Functionality for the vertical hospital
    """,
    'author': "cmanuel.alvarez11@gmail.com",
    'website': "",
    'category': '',
    'version': '16.0.1',
    'depends': [
        'base',
        'mail'
    ],
    'data': [
        # Security
        'security/ir.model.access.csv',
        #Data
        'data/ir_sequence_data.xml',
        # Views
        'views/menuitems.xml',
        'views/patients_views.xml',
        'views/treatments_views.xml',
        'views/res_config_settings_views.xml',
        # Report
        'reports/patients_report.xml'
    ],
    'application': True,
}
