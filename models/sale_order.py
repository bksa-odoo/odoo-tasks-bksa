from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    commision = fields.Boolean("Add Commissions")