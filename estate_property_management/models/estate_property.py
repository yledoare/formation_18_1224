# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Property'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(
        string='Description'
    )
    owner_id = fields.Many2one(
        'res.partner',
        string='Owner',
        required=True
    )
    street = fields.Char('street')
    city = fields.Char('city')
    zip = fields.Char('zip')
    country_id = fields.Many2one('res.country', string='country')
    type = fields.Selection([
        ('appartement', 'Appartement'),
        ('house', 'House'),
        ('office', 'Office'),
    ], string='type')
    tags_ids = fields.Many2many('estate.property.tag', string='Tags')