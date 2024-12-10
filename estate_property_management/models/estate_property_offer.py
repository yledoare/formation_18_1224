# -*- coding: utf-8 -*-

from odoo import models, fields


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Offer for Property'


    property_id = fields.Many2one(
        'estate.property',
        string='Property'
    )
    seller_id = fields.Many2one(
        'res.partner',
        string='Seller'
    )
    buyer_id = fields.Many2one('res.partner', string='Buyer')
    amount = fields.Monetary('Amount')
    currency_id = fields.Many2one(
        'res.currency',
        string='Currency'
    )
    date_of_validity = fields.Datetime('Date Of Validity')