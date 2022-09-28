# -*- coding: utf-8 -*-
{
    'name': "karavan",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'karavan',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
#         'security/karavan_security.xml',
#         'security/ir.model.access.csv',


#         'views/views.xml',
#         'views/sube_view.xml',
#         'views/ilce_view.xml',
# #         'views/okul_view.xml',
# #         'views/takim_view.xml',
#         'views/res_users_views.xml',
#         'views/templates.xml',
#         'views/signup_extra.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
#         'demo/demo.xml',
    ],
}
