from odoo import fields, models, api

class FleetVehicleModelCategory(models.Model):
    _inherit = 'fleet.vehicle.model.category'
    
    max_weight = fields.Integer(string='Max Weight(kg)')
    max_volume = fields.Integer(string='Max Volume(m\u00b3)')
    
    @api.depends('max_weight','max_volume')
    def _compute_display_name(self):
        for record in self:
            name = record.name
            if(record.max_weight or record.max_volume):
               name = f"{record.name} ({record.max_weight}kg, {record.max_volume}m\u00b3)"    
            record.display_name = name   