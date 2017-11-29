"""This module holds the user class"""
from flask import session
USER_LIST = []
class User(object):
    """This class holds methods and attributes for the user"""
    def __init__(self, firstname=None, lastname=None, email=None, password=None):
        """This method initializes the attributes"""
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def login(self, email, password):
        """This method is used to login the user"""
        self.email = email
        self.password = password
        if email and password not in USER_LIST:
            return 'Invalid User.Have you registered'

        session['email'] = email
        session['password'] = password
        return False

    def register(self, firstname, lastname, email, password):
        """This method is used to register a user"""
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        if email in USER_LIST:
            return 'The email is already registered please use another email'
        else:
            USER_LIST.append(firstname)
            USER_LIST.append(lastname)
            USER_LIST.append(email)
            USER_LIST.append(password)
        return False
