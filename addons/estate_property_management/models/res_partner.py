from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Add your custom fields and methods here
    property_ids = fields.One2many('estate.property', 'owner_id', string='Properties')
    offer_count = fields.Integer(
        string='Number of Offers',
        compute='_compute_offer_count'
    )

    def _compute_offer_count(self):
        for partner in self:
            partner.offer_count = self.env['estate.offer'].search_count([('buyer_id', '=', partner.id)])
    
