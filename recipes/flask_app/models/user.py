from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.__init__ import DATABASE
from flask_app import app
import re
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$')



class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * "
        query += "FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []

        for user in results:
            users.append((user))
        return users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * "
        query += "FROM users "
        query += "WHERE email=%(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
        
    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * "
        query += "FROM users "
        query += "WHERE id=%(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])


    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO users(first_name, last_name, email, password) "
        query += "VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['first_name']) < 1:
            is_valid = False
            flash("First name must be at least one character", "error_first_name")
        if len(data['last_name']) < 1:
            is_valid = False
            flash("Last name must be at least one character", "error_last_name")
        if not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Invalid email address", "error_email")
        if User.get_one(data) != False:
            is_valid = False
            flash("Username already exists", "error_email")
        if not PASSWORD_REGEX.match(data['password']):
            is_valid = False
            flash("Password must be at least 8 characters long, and contain at least one uppercase, one lowercase, one number, and one symbol", "error_password")
        if data['password'] != data['confirm_password']:
            is_valid = False
            flash("Password and Confirm Password did not match", "error_confirm_password")
        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True
        if data['password'] == False:
            is_valid = False
            flash("Email and Password did not match", "error_passwords")
        return is_valid
