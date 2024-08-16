# Gym Progress Report Model 
from odoo import models, fields

class GymProgressReport(models.Model):
    _name = 'gym.progress.report'
    _description = 'Gym Progress Report'

    member_id = fields.Many2one('gym.member', string='Member', required=True)
    report_date = fields.Date(string='Report Date', default=fields.Date.today)
    workout_summary = fields.Text(string='Workout Summary')
    nutrition_summary = fields.Text(string='Nutrition Summary')
    body_composition_summary = fields.Text(string='Body Composition Summary')
