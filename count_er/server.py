from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def count_er():
    if "num_of_visits" in session:
        session["num_of_visits"] += 1
    else:
        session["num_of_visits"] = 1
    return render_template("index.html")

@app.route("/destroy_session")
def clear_counter():
    session["num_of_visits"] = 0
    return redirect("/")

@app.route("/counter_plus_two")
def counter_plus_2():
    if "num_of_visits" in session:
        session["num_of_visits"] += 1
    else:
        session["num_of_visits"] = 1
    return redirect("/")



if __name__ == "__main__":
    app.run(debug = True)