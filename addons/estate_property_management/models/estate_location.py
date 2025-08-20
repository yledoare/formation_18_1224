# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EstateLocation(models.Model):
    _name = 'estate.location'
    _inherit = [
        'mail.thread',
        'mail.activity.mixin',
        'image.mixin',
        'estate.commission.mixin'
    ]
    _description = 'Contract Location'

    name = fields.Char('Name')
    property_id = fields.Many2one('estate.property', string='Property')
    description = fields.Text('Description')
    customer_id = fields.Many2one('res.partner', string='Customer')
    bailleur_id = fields.Many2one('res.partner', string='Bailleur')
    seller_id = fields.Many2one('res.users', string='Seller')
    amount = fields.Float('Amount')
    amount_commission = fields.Float('Amount Commission')
    amount_net = fields.Float('Amount Net')

    @api.onchange('property_id')
    def _onchange_property_id(self):
        if self.property_id:
            if self.property_id.owner_id:
                self.description = self.property_id.owner_id.name + ' - ' + self.property_id.name + 'Super dynamic description'
    
    def rainbow(self):
        self.ensure_one()
        self.description = self.description + '🌈'
        marge, amount_commisison = self.get_commission_marge(amount=self.amount)
        self.amount_commission = amount_commisison
        self.amount_net = marge
        return {
            'effect': {
                'fadeout': 'slow',
                'message': '🌈 Rainbowfied! 🌈'
            }
        }