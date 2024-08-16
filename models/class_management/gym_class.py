# Gym Class Model 
from odoo import models, fields

class GymClass(models.Model):
    _name = 'gym.class'
    _description = 'Gym Class'

    name = fields.Char(string='Class Name', required=True)
    schedule_time = fields.Datetime(string='Schedule Time', required=True)
    duration = fields.Float(string='Duration (hours)', required=True)
    trainer_id = fields.Many2one('gym.trainer', string='Trainer')
    max_participants = fields.Integer(string='Max Participants')
    booked_members_ids = fields.Many2many('gym.member', string='Booked Members', readonly=True)

