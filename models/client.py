from odoo import api, fields, models


class ClientModel(models.Model):
    _name = 'client.model'
    _description = 'Client Model'
    image = fields.Image(string='Image')
    name = fields.Char(string='Name')
    cin = fields.Char(string='CIN')
    date_naissance = fields.Date(string='Date de naissance')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')
    sexe = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Sexe')


