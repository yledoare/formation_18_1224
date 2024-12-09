from odoo import models, fields

class MaClass(models.Model):
    _name = 'ma.class'
    _description = 'Ma Class'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    date = fields.Date(string='Date')
    