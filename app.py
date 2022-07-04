from crypt import methods
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "tibiraboto_1234567"

@app.route('/hello')
def index():
    flash("what's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    name = request.form['name_input']
    flash("Hi "+ str(name) + ", great see you!!!" )
    return render_template("index.html")

