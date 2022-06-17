from flask_app import app
from flask import Flask, render_template, request, redirect, session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
@app.route("/dojos")
def home_page():
    return render_template("dojos.html", dojos=Dojo.get_all())

@app.route("/dojos/update", methods = ["POST"])
def create_new_dojo():
    data = {
        "dojo_name": request.form["dojo_name"]
    }
    Dojo.save_dojo(data)
    return redirect("/dojos")


@app.route("/dojos/<int:id>")
def display_ninjas(id):
    data = {
        "dojo_id": id
    }
    data_2 = {
        "dojo_id": id
    }
    return render_template("ninjas_in_dojos.html", ninjas=Ninja.get_all(data), one_dojo=Dojo.get_one(data_2), id = id)