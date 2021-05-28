# -*- coding: utf-8 -*-

from odoo import models, fields, api


class itimodule1(models.Model):
    _name = 'itimodule1.itimodule1'
    _description = 'itimodule1.itimodule1'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float()
    description = fields.Text()

