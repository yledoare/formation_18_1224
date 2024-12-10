from random import randint
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate Property Tag'
    _parent_store = True

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(required=True)
    parent_id = fields.Many2one('estate.property.tag', string='Parent Tag', index=True)
    child_ids = fields.One2many('estate.property.tag', 'parent_id', string='Child Tags')
    color = fields.Integer(string='Color', default=_get_default_color, aggregator=False)
    parent_path = fields.Char(index=True)

    @api.constrains('parent_id')
    def _check_parent_id(self):
        if self._has_cycle():
            raise ValidationError(_('You can not create recursive tags.'))

    @api.depends('parent_id')
    def _compute_display_name(self):
        """ Return the categories' display name, including their direct
            parent by default.
        """
        for tag in self:
            names = []
            current = tag
            while current:
                names.append(current.name or "")
                current = current.parent_id
            tag.display_name = ' / '.join(reversed(names))
