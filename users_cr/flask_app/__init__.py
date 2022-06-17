# __init__.py
from flask import Flask, render_template, request, redirect, session
from flask_app.models.users import Users
app = Flask(__name__)
app.secret_key = "secret"
