from odoo import models, fields, api

class EstatePropertyMassOffer(models.TransientModel):
    _name = 'estate.property.mass.offer'
    _description = 'Mass Offer'

    buyer_id = fields.Many2one('res.partner', string='Buyer', required=True)
    offer_amount = fields.Float(string='Offer Amount', required=True)
    property_ids = fields.Many2many('estate.property', string='Properties')

    def default_get(self, fields):
        result = super(EstatePropertyMassOffer, self).default_get(fields)
        active_ids = self._context.get('active_ids')
        active_model = self._context.get('active_model')
        if active_model == 'estate.property' and active_ids:
            result['property_ids'] = [(6, 0, active_ids)]
        return result

    def action_apply(self):
        for record in self:
            offer_vals = []
            for property_id in record.property_ids:
                offer_vals.append({
                    'property_id': property_id.id,
                    'buyer_id': record.buyer_id.id,
                    'amount': record.offer_amount,
                })
        self.env['estate.property.offer'].create(offer_vals)
    
    # def action_apply(self):
    #     for record in self:
    #         for property_id in record.property_ids:
    #             self.env['estate.property.offer'].create({
    #                 'property_id': property_id.id,
    #                 'buyer_id': record.buyer_id.id,
    #                 'amount': record.offer_amount,
    #             })