from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret"


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/submit_form", methods = ["POST"])
def create_info():
    session["user_name"] = request.form["yourname"]
    session["dojo_loc"] = request.form["dojolocation"]
    session["favorite_lang"] = request.form["favoritelanguage"]
    session["comm"] = request.form["comment"]
    return redirect("/submitted_info")

@app.route("/submitted_info")
def sub_info():
    return render_template("submitted_info.html")



if __name__ == "__main__":
    app.run(debug = True)