# -*- coding: utf-8 -*-
# from odoo import http


# class Karavan(http.Controller):
#     @http.route('/karavan/karavan', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/karavan/karavan/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('karavan.listing', {
#             'root': '/karavan/karavan',
#             'objects': http.request.env['karavan.karavan'].search([]),
#         })

#     @http.route('/karavan/karavan/objects/<model("karavan.karavan"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('karavan.object', {
#             'object': obj
#         })
