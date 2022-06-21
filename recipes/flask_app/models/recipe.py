from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.__init__ import DATABASE
from flask_app import app

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made_on = data['date_made_on']
        self.under_30_min = data['under_30_min']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * from recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        recipes = []

        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def get_one(cls, data):
        query = "SELECT * "
        query += "FROM recipes "
        query += "WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])

    @classmethod
    def add_recipe(cls, data):
        query = "INSERT INTO recipes(name, description, instructions, date_made_on, under_30_min, user_id) "
        query += "VALUES(%(name)s, %(description)s, %(instructions)s, %(date_made_on)s, %(under_30_min)s, %(user_id)s);"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results

    @classmethod
    def update_recipe(cls, data):
        query = "UPDATE recipes "
        query += "SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_made_on = %(date_made_on)s, under_30_min = %(under_30_min)s "
        query += "WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def remove_recipe(cls, data):
        query = "DELETE FROM recipes "
        query += "WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 1:
            is_valid = False
            flash("Name must be at least one character", "error_name")
        if len(data['description']) < 1:
            is_valid = False
            flash("Description must be at least one character", "error_description")
        if len(data['instructions']) < 1:
            is_valid = False
            flash("Instructions must be at least one character", "error_instructions")
        if len(data['date_made_on']) < 1:
            is_valid = False
            flash("Must pick a date", "error_date_made_on")
        if 'toggle' not in data:
            flash("Must select 'Yes' or 'No'", "error_under_30_min")
            is_valid = False
        return is_valid
