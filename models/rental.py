from odoo import api, models, fields


class Rental(models.Model):
    _name = 'rental.model'
    _description = 'location des equipements'

    client_id = fields.Many2one('client.model', string='Client', required=True)
    equipement_id = fields.Many2one('equipement.model', string='Equipement', required=True, domain="[('status','=','available')]")
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    total_price = fields.Float(string='Total Price', readonly=True, compute='_compute_total_price', store=True)
    status = fields.Selection([
        ('rented', 'Rented'),
        ('returned', 'Returned')
    ], string='Status', default='rented', required=True)

    @api.depends('equipement_id.price', 'start_date', 'end_date')
    def _compute_total_price(self):
        for rental in self:
            if rental.equipement_id and rental.start_date and rental.end_date:
                rental_days = (rental.end_date - rental.start_date).days + 1
                rental.total_price = rental_days * rental.equipement_id.price
            else:
                rental.total_price = 0.0

    @api.model
    def create(self, vals):
        rental = super(Rental, self).create(vals)
        if rental.equipement_id:
            rental.equipement_id.status = 'rented'

        invoice = self.env['equipement.invoice'].create({
            'rental_id': rental.id,
            'client_id': rental.client_id.id,
            'equipement_id': rental.equipement_id.id,
            'rental_date': rental.start_date,
            'return_date': rental.end_date,
            'total_price': rental.total_price,
        })
        return rental

    def write(self, vals):
        res = super(Rental, self).write(vals)
        if 'status' in vals and vals['status'] == 'returned':
            for rental in self:
                if rental.equipement_id:
                    rental.equipement_id.status = 'available'
        else:
            for rental in self:
                if rental.equipement_id:
                    rental.equipement_id.status = 'rented'
        return res
