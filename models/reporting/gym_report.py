# Gym Report Model 
from odoo import models, fields

class GymReport(models.Model):
    _name = 'gym.report'
    _description = 'Gym Report'

    report_name = fields.Char(string='Report Name', required=True)
    generated_on = fields.Datetime(string='Generated On', default=fields.Datetime.now)
    data_summary = fields.Text(string='Data Summary')
