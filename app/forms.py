from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Email, InputRequired


class User(object):
      def __init__(self,firstname,lastname,email,username,userpassword):
          self.firstname=firstname
          self.lastname=lastname
          self.email=email
          self.username=username
          self.userpassword=userpassword
 

class Register(FlaskForm):           
 regfirstname = StringField('First name', validators=[InputRequired()])
 reglastname = StringField('Last name', validators=[InputRequired()])
 regemail = StringField('E-mail', validators=[InputRequired(), Email('Invalid Email')])
 regusername = StringField('Username', validators=[InputRequired()])
 regpassword = PasswordField('Password', validators=[InputRequired()])

    
