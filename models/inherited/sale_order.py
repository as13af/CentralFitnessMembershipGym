# Inherited Sale Order Model 
from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    membership_plan_id = fields.Many2one('gym.membership.plan', string='Membership Plan')
    gym_member_id = fields.Many2one('gym.member', string='Gym Member')
