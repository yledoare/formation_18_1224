# -*- coding: utf-8 -*-

from odoo import models, fields, api

def action_send_mail(self):
#   template = self.env.ref(“module_name.email_template_name”)
#   email_values = {'email_from': self.env.user.email}
#   template.send_mail(self.id, force_send=True, email_values=email_values)
    print("OK")

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Property'
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name) ', 'The name of the property must be unique')
    ]

    name = fields.Char(string='Name', required=True)
    description = fields.Text(
        string='Description',
        translate=True,
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
    is_sold = fields.Boolean('Is Sold')
    image = fields.Binary(
        attachment=True, help="This field holds the photo of the property."
    )    
