from odoo import fields, models, api

class SaleOrderLines(models.Model):
    _inherit = 'sale.order.line'
    
    commission_lines = fields.Float('Commission')
    
    
   