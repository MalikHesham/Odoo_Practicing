from odoo import models, fields
class PharmacyMedicine(models.Model):
    _name = 'pharmacy_medicine'
    _description = 'medicine and medical supplies'

    name = fields.Char('Name', required=True)
    description = fields.Text('Description', required=True, )
    manufacturer = fields.Char('Manufactured By: ',required=True, )
    price= fields.Float(string='Price: ')

