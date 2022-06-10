from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play")
@app.route("/play/<x>")
@app.route("/play/<x>/<color>")
def play_x_color(x=3, color="lightblue"):
    return render_template("level3.html", box_num = int(x), box_color = color)

if __name__ == "__main__":
    app.run(debug = True)
