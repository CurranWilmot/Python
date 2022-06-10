from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<x>")
@app.route("/<x>/<y>")
@app.route("/<x>/<y>/<color1>")
@app.route("/<x>/<y>/<color1>/<color2>")
def check_x_y_color(x=8, y=8, color1="red", color2="black"):
    return render_template("index.html", b_width = int(x), b_height = int(y), color_1 = str(color1), color_2 = str(color2))



if __name__ == "__main__":
    app.run(debug = True)