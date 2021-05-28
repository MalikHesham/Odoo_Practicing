# -*- coding: utf-8 -*-
# from odoo import http


# class Itimodule1(http.Controller):
#     @http.route('/itimodule1/itimodule1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/itimodule1/itimodule1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('itimodule1.listing', {
#             'root': '/itimodule1/itimodule1',
#             'objects': http.request.env['itimodule1.itimodule1'].search([]),
#         })

#     @http.route('/itimodule1/itimodule1/objects/<model("itimodule1.itimodule1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('itimodule1.object', {
#             'object': obj
#         })
