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
    'version': '12.0.1.1.0',

    # any module necessary for this one to work correctly
    'depends': ['website_sale','website_theme_install', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    #    'views/views.xml',
    #    'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}