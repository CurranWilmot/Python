from flask import Flask, render_template, request, redirect, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
app = Flask(__name__)
app.secret_key = "secret"