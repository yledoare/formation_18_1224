# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EstateLocation(models.Model):
    _name = 'estate.location'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Contract Location'

    name = fields.Char('Name')
    property_id = fields.Many2one('estate.property', string='Property')
    customer_id = fields.Many2one('res.partner', string='Customer')
    bailleur_id = fields.Many2one('res.partner', string='Bailleur')
    seller_id = fields.Many2one('res.users', string='Seller')
    amount = fields.Float('Amount')