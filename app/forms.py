from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Email, InputRequired
from flask_login import UserMixin


class RegisterForm(FlaskForm):
    regfirstname = StringField('regfirstname', validators=[InputRequired()])
    reglastname = StringField('reglastname', validators=[InputRequired()])
    regemail = StringField('regemail', validators=[InputRequired(), Email('Invalid Email')])
    regusername = StringField('regusername', validators=[InputRequired()])
    regpassword = PasswordField('regpassword', validators=[InputRequired()])

