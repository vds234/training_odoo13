# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Training',
    'version' : '1.1',
    'summary': 'Training',
    'sequence': 15,
    'description': """Training
    """,
    'category': 'Training',
    'website': 'https://www.odoo.com/page/billing',
    'images' : [],
    'depends' : ['base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_details_view.xml',
        'views/teacher_details_view.xml',
        'views/principal_details_view.xml',
        'views/student_line_view.xml',
        'views/menu_item.xml',


    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
