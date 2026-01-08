# -*- coding: utf-8 -*-
# from odoo import http


# class GestionHospital(http.Controller):
#     @http.route('/gestion_hospital/gestion_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_hospital/gestion_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_hospital.listing', {
#             'root': '/gestion_hospital/gestion_hospital',
#             'objects': http.request.env['gestion_hospital.gestion_hospital'].search([]),
#         })

#     @http.route('/gestion_hospital/gestion_hospital/objects/<model("gestion_hospital.gestion_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_hospital.object', {
#             'object': obj
#         })

