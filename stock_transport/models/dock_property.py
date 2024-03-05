from odoo import fields, models

class Dock(models.Model):
    _name = "dock.property"
    _description = "Fleets Dock Name"
    
    name=fields.Char(string="Dock")
    
    