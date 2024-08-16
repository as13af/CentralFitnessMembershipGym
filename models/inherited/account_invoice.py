# Inherited Account Invoice Model 
from odoo import models, fields

class AccountInvoice(models.Model):
    _inherit = 'account.move'

    gym_member_id = fields.Many2one('gym.member', string='Gym Member')
    membership_plan_id = fields.Many2one('gym.membership.plan', string='Membership Plan')
    total_amount = fields.Float(string='Total Amount')
