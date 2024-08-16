# Gym Workout History Model 
from odoo import models, fields

class GymWorkoutHistory(models.Model):
    _name = 'gym.workout.history'
    _description = 'Gym Workout History'

    member_id = fields.Many2one('gym.member', string='Gym Member', required=True)
    workout_date = fields.Date(string='Workout Date', required=True)
    exercises_done = fields.Text(string='Exercises Done')
    total_calories_burned = fields.Float(string='Total Calories Burned', compute='_compute_total_calories_burned', store=True)

    @api.depends('workout_exercise_ids.calories_burned')
    def _compute_total_calories_burned(self):
        for record in self:
            record.total_calories_burned = sum(exercise.calories_burned for exercise in record.workout_exercise_ids)

    workout_exercise_ids = fields.One2many('gym.workout.exercise', 'workout_history_id', string='Workout Exercises')