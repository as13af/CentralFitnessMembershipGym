# Gym Access Control Model 
from odoo import models, fields

class GymAccessControl(models.Model):
    _name = 'gym.access.control'
    _description = 'Gym Access Control'

    member_id = fields.Many2one('gym.member', string='Gym Member', required=True)
    otp_code = fields.Char(string='OTP Code', required=True)
    access_time = fields.Datetime(string='Access Time', default=fields.Datetime.now)
    status = fields.Selection([
        ('granted', 'Granted'),
        ('denied', 'Denied')
    ], string='Status', required=True)
