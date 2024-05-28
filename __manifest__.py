# -*- coding: utf-8 -*-
{
    'name': "location_equipements",
    'summary': "Module de gestion de location des equipements",
    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'location',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
     'data': [

        'views/client_view.xml',
        'views/equipement_view.xml',
        'views/rental_view.xml',
        'views/invoice_view.xml',
        'security/ir.model.access.csv',
        'report/client_report_template.xml',
        'report/client_report.xml',
         'report/report_invoice.xml',
        'report/invoice_report_template.xml',
         'views/dashboard_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
