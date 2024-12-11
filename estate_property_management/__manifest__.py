# -*- coding: utf-8 -*-
{
    'name': "estate_property_management",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'contacts',
    ],

    # always loaded
    'data': [
        # DATA
        'data/estate_property_offer_state.xml',
        # SECURITY
        'security/res_groups.xml',
        'security/ir_rule.xml',
        'security/ir.model.access.csv',
        # VIEWS
        'views/estate_property_views.xml',
        'views/estate_property_tag_views.xml',
        'views/res_partner_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_offer_state_views.xml',
        'views/estate_location.xml',
        # WIZARD
        'wizard/mass_offer_views.xml',
        'wizard/estate_property_mass_tag_views.xml',
        #REPORT
        'report/estate_location_report.xml',
        'report/estate_location_report_template.xml',
        # MENU
        'views/menu.xml',
    ],

}

