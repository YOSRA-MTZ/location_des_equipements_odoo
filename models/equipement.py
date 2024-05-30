from odoo import api, models, fields


class Equipement(models.Model):
    _name = 'equipement.model'
    _description = 'location des equipements'

    rental_ids = fields.One2many('rental.model', 'equipement_id', string='Rentals')

    image = fields.Image("Image", max_width=128, max_height=128)
    equipement_number = fields.Char(string='Equipement Number', required=True)
    name = fields.Char(string='Name')
    model = fields.Char(string='Model')
    price = fields.Float(string='Price per Day')
    status = fields.Selection([
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('under maintenance', 'Under maintenance'),
    ], string='Status', default='available', readonly=True)
