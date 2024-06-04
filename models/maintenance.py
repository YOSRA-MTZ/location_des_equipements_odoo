from odoo import models, fields, api

class EquipmentMaintenance(models.Model):
    _name = 'rental.maintenance'
    _description = 'Equipment Maintenance'

    equipement_id = fields.Many2one('equipement.model', string='Equipement', required=True, domain="[('status','=','available')]")
    maintenance_date = fields.Date(string='Maintenance Date', required=True)
    description = fields.Text(string='Description')
    cost = fields.Float(string='Cost')
    status = fields.Selection([
        ('under maintenance', 'under maintenance'),
        ('maintained', 'maintained')
    ], string='Status', default='under maintenance', required=True)

    @api.model
    def create(self, vals):
        maint = super(EquipmentMaintenance, self).create(vals)
        if maint.equipement_id:
            maint.equipement_id.status = 'under maintenance'
        return maint


    def write(self, vals):
        res = super(EquipmentMaintenance, self).write(vals)
        if 'status' in vals and vals['status'] == 'maintained':
            for maintenance in self:
                if maintenance.equipement_id:
                    maintenance.equipement_id.status = 'available'
        else:
            for maintenance in self:
                if maintenance.equipement_id:
                    maintenance.equipement_id.status = 'under maintenance'
        return res
