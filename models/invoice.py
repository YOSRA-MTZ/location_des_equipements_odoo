from odoo import fields, models,api


class Invoice(models.Model):
    _name = 'equipement.invoice'
    _description = 'location des equipements'
    rental_id = fields.Many2one('rental.model', string='Rental')
    client_id = fields.Many2one('client.model', string='Client', related='rental_id.client_id'  )
    equipement_id = fields.Many2one('equipement.model', string='Equipement', related='rental_id.equipement_id')
    rental_date = fields.Date(string='Rental Date', related='rental_id.start_date')
    return_date = fields.Date(string='Return Date', related='rental_id.end_date')
    total_price = fields.Float(string='Total Price', readonly=True, related='rental_id.total_price')
    status = fields.Selection([
        ('not_paid', 'Not Paid'),
        ('paid', 'Paid')
    ], string='Status', default='not_paid')

    def generate_invoice(self):
        InvoiceObj = self.env['account.move']
        line_items = []
        for invoice in self:
            equipement_price = invoice.equipement_id.price
            total_price = invoice.rental_id.total_price
            line_items.append((0, 0, {
                'name': 'Rental: ' + invoice.rental_id.equipement_id.name,
                'quantity': 1,
                'price_unit': equipement_price,
                'price_subtotal': total_price,
            }))
        invoice_vals = {
            'partner_id': self.client_id.id,
            'invoice_line_ids': line_items,
        }
        invoice = InvoiceObj.create(invoice_vals)

