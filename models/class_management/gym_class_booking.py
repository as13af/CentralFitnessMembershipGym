# Gym Class Booking Model 
from odoo import models, fields

class GymClassBooking(models.Model):
    _name = 'gym.class.booking'
    _description = 'Gym Class Booking'

    member_id = fields.Many2one('gym.member', string='Gym Member', required=True)
    class_id = fields.Many2one('gym.class', string='Gym Class', required=True)
    booking_date = fields.Datetime(string='Booking Date', default=fields.Datetime.now)
    status = fields.Selection([
        ('booked', 'Booked'),
        ('cancelled', 'Cancelled')
    ], string='Status', required=True, default='booked')
