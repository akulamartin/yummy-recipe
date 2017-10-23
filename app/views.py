# views.py

from flask import render_template
from flask_login import login_required 
from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/ForgotPassword', methods=['GET', 'POST'])
def about():
    return render_template("ForgotPassword.html")


@app.route('/Categories', methods=['GET', 'POST'])
@login_required
def Categories():
    return render_template("Categories.html")


@app.route('/UserRegistration', methods=['GET', 'POST'])
def UserRegistration():
    return render_template("UserRegistration.html")


    

