# Copyright (C) 2017 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

{
    'name': 'Lead Line Product',
    'version': '12.0.1.0.1',
    'category': 'Customer Relationship Management',
    'license': 'LGPL-3',
    'summary': 'Adds a lead line in the lead/opportunity model '
               'in odoo',
    'author': "Eficent, Odoo Community Association (OCA)",
    'website': 'https://github.com/OCA/crm',
    'depends': ['crm', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_lead_views.xml',
        'views/crm_lead_line_views.xml',
        'report/crm_product_report_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
