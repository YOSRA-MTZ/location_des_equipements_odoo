# -*- coding: utf-8 -*-
# from odoo import http


# class LocationEquipements(http.Controller):
#     @http.route('/location_equipements/location_equipements', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/location_equipements/location_equipements/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('location_equipements.listing', {
#             'root': '/location_equipements/location_equipements',
#             'objects': http.request.env['location_equipements.location_equipements'].search([]),
#         })

#     @http.route('/location_equipements/location_equipements/objects/<model("location_equipements.location_equipements"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('location_equipements.object', {
#             'object': obj
#         })
