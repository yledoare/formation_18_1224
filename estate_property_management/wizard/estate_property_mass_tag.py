from odoo import models, fields, api

class EstatePropertyMassTag(models.TransientModel):
    _name = 'estate.property.mass.tag'
    _description = 'Mass Tag Properties'

    tags_ids = fields.Many2many(
        'estate.property.tag',
        default=lambda self: self._context.get('active_ids'),
        string='Tags'
    )
    property_ids = fields.Many2many('estate.property', string='Properties')

    def action_apply(self):
        for tag in self.tags_ids:
            self.property_ids.write({'tags_ids': [(4, tag.id)]})