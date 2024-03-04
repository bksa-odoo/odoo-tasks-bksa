from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    commission = fields.Boolean("Add Commissions")
    total_commission = fields.Float('Total Commission', compute="_compute_total_commission", default=0)
    
    @api.depends('order_line.commission_lines')
    def _compute_total_commission(self):
        for order in self:
            total_calculated_commission = sum(line.commission_lines for line in order.order_line)
            if order.commission:
                order.total_commission = total_calculated_commission
            else:
                order.total_commission = 0
            
            
    @api.depends('order_line.price_subtotal', 'order_line.price_tax', 'order_line.price_total', 'total_commission', 'commission')
    def _compute_amounts(self):
        res = super()._compute_amounts()
        # breakpoint()
        for order in self:
            # Default behavior without commission
            order.amount_untaxed = sum(order.order_line.mapped('price_subtotal'))
            order.amount_tax = sum(order.order_line.mapped('price_tax'))
            order.amount_total = order.amount_untaxed + order.amount_tax
            
            # If commission is true, add total_commission to tax and total amount
            if order.commission:
                order.amount_untaxed += order.total_commission
                order.amount_total += order.total_commission
            # If commission is false, keep the default value or subtract it from the value formed after adding total_commission amount
            else:
                # This part is optional and depends on how you want to handle the case when commission is false.
                # For example, if you want to subtract the total_commission from the total amount:]
                order.amount_untaxed -= order.total_commission
                order.amount_total -= order.total_commission
                # Ensure amount_total does not go below zero
                order.amount_total = max(order.amount_total,  0)
            print("amount untaxed from sales commission",order.amount_untaxed)    
            print("amount total from sales commission",order.amount_total)    
        return res        
        
        
