# -*- coding: utf-8 -*-
{
    'name': "B2B Base",

    'summary': """
        B2B Base module for B2B Theme
    """,

    'description': """
        B2B Base module for B2B Theme
    """,

    'author': "Impulso Diagonal",
    'website': "http://impulso.xyz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Web',
    'version': '14.0.1.1.0',

    # any module necessary for this one to work correctly
    'depends': ['website_sale', 'stock'],

    # always loaded
    'data': [
    ],
    # only loaded in demonstration mode
}
