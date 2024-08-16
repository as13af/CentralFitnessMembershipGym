# Gym Member Model 
from odoo import models, fields, api

class GymMember(models.Model):
    _name = 'gym.member'
    _description = 'Gym Member'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    membership_plan_id = fields.Many2one('gym.membership.plan', string='Membership Plan')
    join_date = fields.Date(string='Join Date')
    expiry_date = fields.Date(string='Expiry Date')
    active = fields.Boolean(string='Active', default=True)
    access_token = fields.Char(string='Access Token')
