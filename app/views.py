# views.py

from flask import render_template
from flask_login import login_required,LoginManager 
from .forms import RegisterForm
from app import app

login_manager = LoginManager()
login_manager.init_app(app)

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
    form = RegisterForm()
    if form.validate_on_submit():
     return render_template("Categories.html", form=form)

    return render_template("UserRegistration.html")


    

