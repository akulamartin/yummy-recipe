"""This module holds the category class"""
from flask import session
from .User import User
CATEGORY_LIST = []
class Category(User):
    """This class holds methods and attributes for the category"""
    def __init__(self, name=None, nametochange=None, categoryindex=None):
        """This method initializes the attributes"""
        self.name = name
        self.nametochange = nametochange
        self.categoryindex = categoryindex
        super().__init__(firstname=None, lastname=None, email=None, password=None)

    def add_category(self, name):
        """This method is used to add a category"""
        self.name = name
        category_info = {'Categoryname':name, 'Email':session['email']}
        CATEGORY_LIST.append(category_info)
        return CATEGORY_LIST

    def delete_category(self, categoryindex):
        """This method is used to delete a category"""
        self.categoryindex = categoryindex
        CATEGORY_LIST.remove(CATEGORY_LIST[categoryindex])
        return CATEGORY_LIST

    def edit_category(self, nametochange, categoryindex):
        """This method edits the category name"""
        self.nametochange = nametochange
        CATEGORY_LIST[categoryindex].update({'Categoryname': nametochange})
        return CATEGORY_LIST
