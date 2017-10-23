from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Email, InputRequired
from flask_login import UserMixin


class RegisterForm(FlaskForm):
    regfirstname = StringField('First name', validators=[InputRequired()])
    reglastname = StringField('Last name', validators=[InputRequired()])
    regemail = StringField('E-mail', validators=[InputRequired(), Email('Invalid Email')])
    regusername = StringField('Username', validators=[InputRequired()])
    regpassword = PasswordField('Password', validators=[InputRequired()])

