from flask_app import app
from flask import Flask, render_template, request, redirect, session
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas")
def new_ninjas():
        return render_template("ninjas.html", dojos=Dojo.get_all())

@app.route("/ninjas/create", methods=['POST'])
def create_new_ninja():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"],
        "dojo_name": request.form["dojo_id"]
    }
    print(data)
    Ninja.save_ninja(data)
    return redirect("/dojos")