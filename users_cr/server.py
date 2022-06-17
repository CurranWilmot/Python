
from flask import Flask, render_template, request, redirect, session
from users import Users

app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")
@app.route("/users")
def display_users():
    return render_template("read_all.html",  users=Users.get_all())

@app.route("/users/<int:id>")
def display_user(id):
    data={
        "u_id": id
    }
    one_user = Users.get_one(data)
    return render_template("user_card.html", one_user = one_user)

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
    id = Users.save_user(data)

    return redirect(f"/users/{id}")

@app.route("/users/<int:id>/delete")
def delete_user(id):
    data = {"u_id": id}
    Users.remove_user(data)
    return redirect("/users")

@app.route("/users/<int:id>/edit")
def display_edit_user(id):
    data={
        "u_id": id
    }
    one_user = Users.get_one(data)
    
    return render_template("edit_user_card.html", one_user = one_user)

@app.route("/users/<int:id>/edit/update", methods = ["POST"])
def edit_user(id):
    data = {
        "u_id": id,
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    Users.update_user(data)
    print(f"users/{id}")
    return redirect(f"/users/{id}")

if __name__ == "__main__":
    app.run(debug = True)