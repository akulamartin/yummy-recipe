from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Email, InputRequired


class User(FlaskForm):
        
        regfirstname = StringField('First name', validators=[InputRequired()])
        reglastname = StringField('Last name', validators=[InputRequired()])
        regemail = StringField('E-mail', validators=[InputRequired(), Email('Invalid Email')])
        regusername = StringField('Username', validators=[InputRequired()])
        regpassword = PasswordField('Password', validators=[InputRequired()])

def register_user(self,firstname=None,lastname=None,email=None,username=None,password=None):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.username=username
        self.password=password


    
