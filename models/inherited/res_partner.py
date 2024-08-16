# Inherited Res Partner Model 
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    gym_member_id = fields.Many2one('gym.member', string='Gym Member')
    is_gym_member = fields.Boolean(string='Is Gym Member', compute='_compute_is_gym_member')

    def _compute_is_gym_member(self):
        for record in self:
            record.is_gym_member = bool(record.gym_member_id)