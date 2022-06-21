from flask_app import app
from flask import Flask, flash, render_template, request, redirect, session
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



@app.route("/")
def display_login_register():
    session.clear
    return render_template("login_register.html")




@app.route("/create", methods=["POST"])
def create_user():
    if len(request.form['password']) < 1:
        pw_hash = 1
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form["last_name"],
        'email': request.form["email"],
        'password': pw_hash
    }

    if User.validate_user(request.form) == False:
        return redirect("/")

    else:
        id = User.add_user(data)
        session["user_email"] = request.form["email"]
        return redirect(f"/dashboard/{id}")




@app.route("/login", methods=["POST"])
def login_user():
    email_data = {
        'email': request.form['email']
    }
    this_user = User.get_one(email_data)
    if this_user:
        valid_pass = bcrypt.check_password_hash(this_user.password, request.form["password"])
        data = {
            'password': valid_pass
        }
        if User.validate_login(data) == False:
            return redirect("/")
        else:
            id = this_user.id
            session["user_email"] = request.form["email"]
            return redirect(f"/dashboard/{id}")
    else:
        flash("Username does not exist", "error_user")
        return redirect("/")




@app.route("/dashboard/<int:id>")
def display_dashboard(id):
    if not session:
        return redirect("/")
    recipes = User.get_all()
    data = {
        'email': session['user_email']
    }
    one_user = User.get_one(data)
    return render_template("dashboard.html", id = id, recipes = recipes, one_user = one_user)
    
    


@app.route("/logout")
def logout():
    session.clear()
    return render_template("login_register.html")