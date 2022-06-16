
from flask import Flask, render_template, request, redirect, session
from users import Users

app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")
@app.route("/users")
def display_users():
    return render_template("read_all.html", users=Users.get_all())

@app.route("/users/new")
def display_new_user():
    return render_template("create.html")

@app.route("/users/new/create", methods=["POST"])
def create_new_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    Users.save_user(data)
    return redirect("/users")


if __name__ == "__main__":
    app.run(debug = True)