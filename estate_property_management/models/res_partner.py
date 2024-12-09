from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Add your custom fields and methods here
    property_ids = fields.One2many('estate.property', 'owner_id', string='Properties')
    