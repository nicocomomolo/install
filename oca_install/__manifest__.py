# -*- coding: utf-8 -*-
{
    'name': "oca_install",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends':["base",
"web_export_view",
"report_xlsx",
"mass_editing",
"l10n_es_toponyms",
"l10n_es_partner_mercantil",
"l10n_es_partner",
"l10n_es_aeat_mod111",
"l10n_es_aeat",
"l10n_es_account_bank_statement_import_n43",
"l10n_es_account_balance_report",
"l10n_es_account_asset",
"l10n_es",
"document_page",
"base_partner_sequence",
"base_location_geonames_import",
"base_location",
"account_renumber",
"account_payment_partner",
"account_invoice_currency",
"account_balance_reporting",
"account_invoice_constraint_chronology",
"account_due_list_payment_mode",
"account_tax_balance",
"account_bank_statement_import",
"account_banking_sepa_direct_debit",
"account_banking_pain_base",
"account_banking_mandate",
"account_invoice_refund_link",
],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}