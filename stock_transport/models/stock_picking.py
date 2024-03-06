from odoo import fields, models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    volume = fields.Float(string='Volume', compute='_compute_weight_volume')
    weight = fields.Float(string="Weight", compute='_compute_weight_volume')
    
    @api.depends('move_ids_without_package.move_line_ids.product_id.weight', 'move_ids_without_package.move_line_ids.product_id.volume', 'move_ids_without_package.move_line_ids.move_id.product_uom_qty', 'move_ids_without_package')
    def _compute_weight_volume(self):
     for record in self:
        total_weight = 0
        total_volume = 0
        for move in record.move_ids:
            for move_line in move:
                quantity = move_line.product_qty
                total_weight += move_line.product_id.weight * quantity
                total_volume += move_line.product_id.volume * quantity
        record.weight = total_weight
        record.volume = total_volume