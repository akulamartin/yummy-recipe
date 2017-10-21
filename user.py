#!/usr/bin/env python

class User(object):
    keypair={}
    def __init__(self ,firstname=None ,lastname=None ,username=None ,email=None , password=None):
        """ variables"""
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        kepair={'usrname':username,'pssd':password}
    def get_user_register(self,firstname,lastname,email,username,password):
        if firstname !='' and lastname !='' and email !='' and username!='' and password!='':
           return 1;
        if firstname !='' or lastname !='' or email !='' or username!='' or password!='':
           return 2;
            
        if username not in keypair.keys() and password not in keypair.keys():
           return 3;
        
        

