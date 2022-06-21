from flask_app import app
from flask import Flask, flash, render_template, request, redirect, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)



@app.route("/")
def display_login_register():
    session.clear
    return render_template("login_register.html")




@app.route("/create", methods=["POST"])
def create_user():
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    print(pw_hash)

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form["last_name"],
        'email': request.form["email"],
        'password': pw_hash
    }

    data2 = {
        'first_name': request.form['first_name'],
        'last_name': request.form["last_name"],
        'email': request.form["email"],
        'password': request.form["password"],
        'confirm_password': request.form["confirm_password"]
    }
    if User.validate_user(data2) == False:
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
    if session:
        return render_template("dashboard.html", id = id)
    return redirect("/")
    




# @app.route("/logout")
# def log_off():
#     session.clear
#     return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    flash("logged out")
    return render_template("login_register.html")