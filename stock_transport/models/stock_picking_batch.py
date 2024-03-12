from odoo import fields,models,api

class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'
    
    pillName = fields.Char('Pill Name', compute="_compute_pill_name", store=True)
    dock_id = fields.Many2one('dock.property', string='Dock')
    vehicle_id = fields.Many2one('fleet.vehicle', string='Vehicle')
    vehicle_category_id = fields.Many2one('fleet.vehicle.model.category', string='Vehicle Category')
    total_weight = fields.Float(compute='_compute_total_weight', string='Weight',digits=(16,4), store=True)
    total_volume = fields.Float(compute='_compute_total_volume', string='Volume',digits=(16,4), store=True)
    total_weight_percentage = fields.Float(compute='_compute_total_weight', string='Weight Percentage', digits=(16,4), store=True)
    total_volume_percentage = fields.Float(compute='_compute_total_volume', string='Volume Percentage',digits=(16,4), store=True)
    picking_lines = fields.Float(string="Lines", compute='_compute_picking_lines', store=True)
    transfer_lines = fields.Float(string="Transfer", compute='_compute_transfer_lines', store=True)
    date_from = fields.Date('Date From', required=True, index=True,default=fields.Date.context_today)
    date_to = fields.Date('Date To', required=True, index=True, default=fields.Date.context_today)
    
    
    
    @api.depends('picking_ids.weight', 'vehicle_category_id')
    def _compute_total_weight(self):
        for batch in self:
            total_weight = 0
            if batch.vehicle_category_id:
                max_weight = batch.vehicle_category_id.max_weight 
                for picking in batch.picking_ids:
                    total_weight += picking.weight
                batch.total_weight = total_weight       
                batch.total_weight_percentage = (total_weight / max_weight) * 100 if batch.vehicle_category_id.max_weight != 0 else 1
            
            
    @api.depends('picking_ids.volume', 'vehicle_category_id')
    def _compute_total_volume(self):
        for batch in self:
            total_volume = 0
            if batch.vehicle_category_id:
                max_volume = batch.vehicle_category_id.max_volume 
                for picking in batch.picking_ids:
                    total_volume += picking.volume
                batch.total_volume = total_volume      
                batch.total_volume_percentage = (total_volume / max_volume) * 100  if batch.vehicle_category_id.max_volume != 0 else 1
    
    @api.depends("picking_ids")
    def _compute_transfer_lines(self):
        for record in self:
            record.transfer_lines = len(record.picking_ids)

    @api.depends("move_line_ids")
    def _compute_picking_lines(self):
        for record in self:
            record.picking_lines = len(record.move_line_ids)      
            
    # @api.depends('name','total_weight','total_volume')
    # def _compute_display_name(self):
    #     for record in self:       
    #         record.display_name =  f"{record.name} {record.total_weight}kg, {record.total_volume}m\u00b3"
    
    
    @api.depends('name','total_weight','total_volume')
    def _compute_pill_name(self):
        for record in self:       
            record.pillName =  f"{record.name} {record.total_weight}kg, {record.total_volume}m\u00b3"
                
                
            

    
   