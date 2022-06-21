from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.__init__ import DATABASE
from flask_app import app
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$')

#PASSWORD_REGEX = re.compile(r"^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$")

#PASSWORD_REGEX = re.compile(r'^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%#?&])[A-Za-z\d@$!#%?&]{6,20}$')

#from re import compile, VERBOSE

# regex = compile("""
# ^              # begin word
# (?=.?[a-z])   # at least one lowercase letter
# (?=.?[A-Z])   # at least one uppercase letter
# (?=.*?[0-9])   # at least one number
# [A-Za-z\d]     # only alphanumeric
# {6,}           # at least 6 characters long
# $              # end word
# """, VERBOSE)

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
    def get_one(cls, data):
        query = "SELECT * "
        query += "FROM user "
        query += "WHERE email=%(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])


    @classmethod
    def add_user(cls, data):
        query = "INSERT INTO user(first_name, last_name, email, password) "
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
            flash("Password and Confirm Password did not match", "error_password")
        if len(data['password']) < 4:
            is_valid = False
            flash("Password must be at least 4 characters", "error_password")
        return is_valid

    @staticmethod
    def validate_login(data):
        is_valid = True
        if data['password'] == False:
            is_valid = False
            flash("Email and Password did not match", "error_passwords")
        return is_valid
