from odoo import models, fields, api

class orders(models.Model):
    _name = 'orders'
    _description = 'orders'
    
    name = fields.Many2one('res.partner')
    order_lines = fields.One2many("order_lines","order")
    total = fields.Float(compute='_compute')
    date = fields.Date()
    
    @api.onchange('order_lines')
    def _compute(self):
        for line in self:
            sum_l = 0
            for i in line.order_lines:
                sum_l = sum_l+i.sub_total
            line.total = sum_l