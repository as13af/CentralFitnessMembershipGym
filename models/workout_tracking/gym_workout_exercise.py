# Gym Workout Exercise Model 
from odoo import models, fields
class GymWorkoutExercise(models.Model):
    _name = 'gym.workout.exercise'
    _description = 'Gym Workout Exercise'

    workout_history_id = fields.Many2one('gym.workout.history', string='Workout History', required=True)
    exercise_name = fields.Char(string='Exercise Name', required=True)
    sets = fields.Integer(string='Sets', required=True)
    reps = fields.Integer(string='Reps', required=True)
    weight = fields.Float(string='Weight (kg)')
    calories_burned = fields.Float(string='Calories Burned', required=True)