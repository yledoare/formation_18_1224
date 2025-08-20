from odoo import models, fields, api

class EstateCommissionMixin(models.AbstractModel):
    _name = 'estate.commission.mixin'
    _description = 'Abstract Commission Mixin'

    marge = fields.Float('Marge')
    commission = fields.Float('Commission %')
    test = fields.Float('Test')

    def get_commission_marge(self, amount):        
        amount_commission = amount * self.commission / 100
        marge = amount - amount_commission
        return marge, amount_commission