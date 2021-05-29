# -*- coding: utf-8 -*-
{
    'name': "Amazing Library",

    'summary': """
        Manage books easily and accurately with this module """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Malik",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [   'views/library_book.xml',
                'security/groups.xml',
                'security/ir.model.access.csv',
        ],

}
