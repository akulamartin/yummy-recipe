# views.py

from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ForgotPassword')
def about():
    return render_template("ForgotPassword.html")

@app.route('/Categories')
def Categories():
    return render_template("Categories.html")

@app.route('/UserRegistration')
def UserRegistration():
    return render_template("UserRegistration.html")


    

