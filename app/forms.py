from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import Email, InputRequired

userlist={}
class User(object):
 def __init__(self,firstname=None,lastname=None,email=None,username=None,userpassword=None):
          self.firstname=firstname
          self.lastname=lastname
          self.email=email
          self.username=username
          self.userpassword=userpassword

 def register_User(self,firstname,lastname,email,username,userpassword):
            userlist = {'firstname': firstname,
                    'lastname': lastname, 'email': email, 'username': username, 'userpassword': userpassword}
               
 def login_User(self,theusername,thepassword):
    if theusername in userlist.values():
     if thepassword==userlist.get(theusername):
      return True
    return False           
             

class Registration(FlaskForm):           
 regfirstname = StringField('First name', validators=[InputRequired()])
 reglastname = StringField('Last name', validators=[InputRequired()])
 regemail = StringField('E-mail', validators=[InputRequired(), Email('Invalid Email')])
 regusername = StringField('Username', validators=[InputRequired()])
 regpassword = PasswordField('Password', validators=[InputRequired()])

    
