# -*- coding: utf-8 -*-

from odoo import models, fields


class EstatePropertyOfferState(models.Model):
    _name = 'estate.property.offer.state'
    _description = 'State For Offer'


    name = fields.Char('name')
    is_sale = fields.Boolean('Is Sale')