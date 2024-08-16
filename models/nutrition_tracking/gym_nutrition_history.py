# Gym Nutrition History Model 
from odoo import models, fields, api

class GymNutritionHistory(models.Model):
    _name = 'gym.nutrition.history'
    _description = 'Gym Nutrition History'

    member_id = fields.Many2one('gym.member', string='Gym Member', required=True)
    log_date = fields.Date(string='Log Date', required=True)
    meals = fields.Text(string='Meals')
    total_calories = fields.Float(string='Total Calories', compute='_compute_total_nutrition', store=True)
    protein = fields.Float(string='Protein (g)', compute='_compute_total_nutrition', store=True)
    carbs = fields.Float(string='Carbs (g)', compute='_compute_total_nutrition', store=True)
    fats = fields.Float(string='Fats (g)', compute='_compute_total_nutrition', store=True)

    @api.depends('nutrition_meal_ids.calories', 'nutrition_meal_ids.protein', 'nutrition_meal_ids.carbs', 'nutrition_meal_ids.fats')
    def _compute_total_nutrition(self):
        for record in self:
            record.total_calories = sum(meal.calories for meal in record.nutrition_meal_ids)
            record.protein = sum(meal.protein for meal in record.nutrition_meal_ids)
            record.carbs = sum(meal.carbs for meal in record.nutrition_meal_ids)
            record.fats = sum(meal.fats for meal in record.nutrition_meal_ids)

    nutrition_meal_ids = fields.One2many('gym.nutrition.meal', 'nutrition_history_id', string='Nutrition Meals')


class GymNutritionMeal(models.Model):
    _name = 'gym.nutrition.meal'
    _description = 'Gym Nutrition Meal'

    nutrition_history_id = fields.Many2one('gym.nutrition.history', string='Nutrition History', required=True)
    meal_name = fields.Char(string='Meal Name', required=True)
    calories = fields.Float(string='Calories', required=True)
    protein = fields.Float(string='Protein (g)')
    carbs = fields.Float(string='Carbs (g)')
    fats = fields.Float(string='Fats (g)')
