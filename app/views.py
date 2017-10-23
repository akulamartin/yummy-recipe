# views.py

from flask import render_template,request
from flask_login import login_required,LoginManager 
from .forms import User,Registration
from app import app

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
#    user=User()
#    if request.method=="POST":
#        username=request.form['Username']
#        password=request.form['Password']
#        if user.login_User(username,password):
#            return 'All Good'
    return render_template("index.html",)


@app.route('/ForgotPassword', methods=['GET', 'POST'])
def about():
    return render_template("ForgotPassword.html")


@app.route('/Categories', methods=['GET', 'POST'])
@login_required
def Categories():
    return render_template("Categories.html")


@app.route('/UserRegistration', methods=['GET', 'POST'])
def UserRegistration():
    form = Registration()
    #user=User()
    if form.validate_on_submit(): 
     #user.register_User(form.regfirstname,form.reglastname,form.regemail,form.regusername,form.regpassword)       
     return render_template("index.html",message='Success')     
    return render_template("UserRegistration.html",form=form)


app.route('/logout')
def logout():
    return render_template("index.html")
    

