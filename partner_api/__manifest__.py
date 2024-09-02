{
    'name': 'Partner API',
    'version': "17.0.1.2.0",
    'category': 'API',
    'author': 'Franco Leyes',
    'license': 'LGPL-3',
    'depends': ['fastapi', 'contacts'],
    'data': [
        'data/partner_api_data.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
