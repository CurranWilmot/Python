# __init__.py
from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "secret"
DATABASE = "recipes_schema"
