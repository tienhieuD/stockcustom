# -*- coding: utf-8 -*-

{
    'name': "Stock Custom",
    'version': '0.1',
    'author': 'Entrust Developer',
    'maintainer': 'Odoo SA',
    'website': "https://entrustlab.com",
    'license': 'LGPL-3',
    'category': 'Warehouse',
    'sequence': 1,
    'description': """ """,
    'summary': """Custom Return Picking Inventory""",
    'depends': ['base', 'stock', 'sale'],
    'data': [
        'data/report_paperformat.xml',
        'views/report_templates.xml',
        'views/saleorder_report_view.xml',
    ],
    'demo': [],
    'qweb': [],
    # 'js': ['static/src/js/first_module.js',],
    # 'css': ['static/src/css/web_example.css',],
    # 'images': ['static/description/icon.png',],
    'auto_install': False,
    'application': True,
    'installable': True,
    # 'external_dependencies': {'python' : ['usb.core','serial','qrcode']}
    # 'pre_init_hook': 'pre_init_hook',
    # 'post_init_hook': 'post_init_hook',
    # 'uninstall_hook': 'uninstall_hook',
}
