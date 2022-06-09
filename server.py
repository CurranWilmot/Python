from flask import Flask, render_template #importing Flask, Flask is now a class
app = Flask(__name__) #application launch

@app.route("/")
def hello_from_flask():
    return render_template("index.html")
    #Some code here for routes and endpoints

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def say_name(name):
    print("duuuude")
    return "Hi " + str(name) + "!"
    

@app.route("/repeat/<num>/<msg>")

def rpt_msg(num, msg):
    temp_str = ""
    for i in range(0, int(num)):
        temp_str += msg
        temp_str += "      "
    return temp_str

if __name__ == "__main__":
    app.run(debug = True)#this code is needed to run your environment and be in an active state when you run this file.
