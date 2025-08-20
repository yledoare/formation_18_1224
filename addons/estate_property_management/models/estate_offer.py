# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class EstateOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Offer for Property'
    _inherit = ['estate.commission.mixin']
    _sql_constraints = [
        ('check_amount', 'CHECK(amount > 0)', 'The amount must be strictly positive')
    ]

    display_name = fields.Char(
        string='Name',
        compute='_compute_display_name'
    )
    name = fields.Char('Name')
    property_id = fields.Many2one(
        'estate.property',
        string='Property',
        required=True
    )
    seller_id = fields.Many2one(
        'res.partner',
        string='Seller',
        related='property_id.owner_id'
    )
    city_of_property = fields.Char(
        string='City',
        related='property_id.city'
    )
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    amount = fields.Monetary('Amount')
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency'
    )
    offer_date = fields.Datetime(
        string='Date of Offer',
        default=fields.Date.context_today
    )
    validity_date = fields.Datetime(
        string='Validity Date',
        compute='_compute_validity_date',
        store=True,
    )
    offer_state_id = fields.Many2one(
        'estate.property.offer.state',
        string='State'
    )
    is_sale = fields.Boolean(
        string='Is Sale',
        related='offer_state_id.is_sale'
    )

    @api.depends('offer_date')
    def _compute_validity_date(self):
        for offer in self:
            if offer.offer_date:
                offer.validity_date = offer.offer_date + timedelta(days=30)


    def _compute_display_name(self):
        for record in self:
            if record.buyer_id and record.property_id:
                record.display_name = record.property_id.name + ' - ' + record.buyer_id.name
            elif not record.property_id or not record.property_id.name:
                record.display_name = 'OFFRE SANS BIEN'
            else:
                record.display_name = 'SUPER OFFRE POUR' + ' - ' + record.property_id.name
    
    @api.constrains('amount', 'property_id', 'buyer_id')
    def _check_double_offer(self):
        for offer in self:
            existing_offer = self.search([
                ('property_id', '=', offer.property_id.id),
                ('buyer_id', '=', offer.buyer_id.id),
                ('amount', '=', offer.amount),
                ('id', '!=', offer.id)
            ])
            if existing_offer:
                raise ValidationError('You cannot make the same offer twice')

    # PAS BESOIN DE DÉFINIR LES CREATE ILS SONT PAR DÉFAUT, MAIS IL EST POSSIBLE DE SURCHARGER POUR APPLIQUER UNE LOGIQUE MÉTIER      
    # @api.model
    # def create(self, vals):
    #     import pdb; pdb.set_trace()
    
    # @api.model_create_multi
    # def create(self, vals_list):
    #     import pdb; pdb.set_trace()
        
    
    def write(self, vals):
        if 'offer_state_id' in vals:
            offer_state_id = self.env['estate.property.offer.state'].browse(vals['offer_state_id'])
            if offer_state_id.is_sale:
                for record in self:
                    vals['name'] = 'OFFRE ACCEPTÉ' + record.property_id.name
                    record.property_id.is_sold = True
        return super(EstateOffer, self).write(vals)

    # def write(self, vals):
    #     res = super(EstatePropertyOffer, self).write(vals)        
    #     for record in self:
    #         if record.is_sale:
    #             record.property_id.is_sold = True
    #     return res
