# Gym Membership Plan Model 
from odoo import models, fields

class GymMembershipPlan(models.Model):
    _name = 'gym.membership.plan'
    _description = 'Gym Membership Plan'

    name = fields.Char(string='Name', required=True)
    price = fields.Float(string='Price', required=True)
    duration_months = fields.Integer(string='Duration (Months)', required=True)
    description = fields.Text(string='Description')
