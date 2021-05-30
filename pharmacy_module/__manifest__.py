{
'name': "Pharmacy",
'summary': "Manage medicine with ease",
'description': """
Pharmcay Manager
==============
Description related to library.
""",
'author': "Your name",
'website': "http://www.example.com",
'category': 'Uncategorized',
'version': '14.0',
'depends': ['base'],
'data': [
        'security/ir.model.access.csv',
        'views/pharmacy_medicine.xml',
        'views/orders.xml',
        'views/order_lines.xml',
    ],
}