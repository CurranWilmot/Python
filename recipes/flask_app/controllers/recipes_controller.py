from flask_app import app
from flask import Flask, flash, render_template, request, redirect, session
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route("/recipes/<int:re_id>")
def display_one_recipe(re_id):
    if not session:
        return redirect("/")
    data = {
        'id': re_id
    }
    session
    one_recipe = Recipe.get_one(data)
    data2 = {
        'email': session["user_email"]
    }
    one_user = User.get_one(data2)
    return render_template("one_recipe.html", one_recipe = one_recipe, re_id = re_id, one_user = one_user)





@app.route("/recipes/new")
def new_recipe():
    if not session:
        return redirect("/")
    data2 = {
        'email': session["user_email"]
    }
    one_user = User.get_one(data2)
    return render_template("add_recipe.html", one_user = one_user)





@app.route("/recipes/new/create", methods=["POST"])
def add_new_recipe():
    data2 = {
        'email': session["user_email"]
    }
    if Recipe.validate_recipe(request.form) == False:
            return redirect("/recipes/new")

    one_user = User.get_one(data2)
    data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made_on': request.form['date_made_on'],
        'under_30_min': request.form['toggle'],
        'user_id': one_user.id
    }
    
    Recipe.add_recipe(data)
    
    return redirect(f"/dashboard/{one_user.id}")




@app.route("/recipes/edit/<int:re_id>")
def edit_recipe(re_id):
    if not session:
        return redirect("/")
    data = {
        'id': re_id
    }
    one_recipe = Recipe.get_one(data)
    data2 = {
        'email': session["user_email"]
    }
    one_user = User.get_one(data2)
    return render_template("edit_recipe.html", re_id = re_id, one_user = one_user, one_recipe = one_recipe)



@app.route("/recipes/edit/<int:re_id>/update", methods=["POST"])
def edit_recipe_update(re_id):
    data2 = {
        'email': session["user_email"]
    }
    one_user = User.get_one(data2)
    if Recipe.validate_recipe(request.form) == False:
            return redirect(f"/recipes/edit/{re_id}")

    data = {
        'id': re_id,
        'name': request.form['name'],
        'description': request.form['description'],
        'instructions': request.form['instructions'],
        'date_made_on': request.form['date_made_on'],
        'under_30_min': request.form['toggle']
    }
    
    Recipe.update_recipe(data)
    
    return redirect(f"/dashboard/{one_user.id}")




@app.route("/recipes/<int:id>/delete")
def delete_recipe(id):
    data2 = {
        'email': session["user_email"]
    }
    one_user = User.get_one(data2)
    data = {"id": id}
    Recipe.remove_recipe(data)
    return redirect(f"/dashboard/{one_user.id}")