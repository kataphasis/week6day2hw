from flask import render_template
from . import bp as app

@app.route("/login")
def contact():
    return render_template('login.html')

@app.route("/register")
def contact():
    return render_template('register.html')