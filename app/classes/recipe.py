"""This module holds the recipe class"""
from flask import session
RECIPE_LIST = []
class Recipe(object):
    """This class holds methods and attributes for the Recipe"""
    def __init__(self, categoryname=None, recipename=None, ingredients=None,
                 method=None):
        """This method initializes the attributes"""
        self.categoryname = categoryname
        self.recipename = recipename
        self.ingredients = ingredients
        self.method = method
        self.recipeindex = 0

    def add_recipe(self, categoryname, recipename, ingredients, method):
        """This method adds a recipe"""
        self.categoryname = categoryname
        self.recipename = recipename
        self.ingredients = ingredients
        self.method = method
        recipe_info = {'Category': categoryname, 'Email':session['email'], 'RecipeName': recipename,
                       'RecipeIngredients': ingredients,
                       'RecipeMethod': method}
        RECIPE_LIST.append(recipe_info)
        return RECIPE_LIST

    def edit_recipe(self, recipeindex, recipename, ingredients, method):
        """This method edits a recipe"""
        self.recipeindex = recipeindex
        self.recipename = recipename
        self.ingredients = ingredients
        self.method = method
        RECIPE_LIST[recipeindex].update({'RecipeName':recipename})
        RECIPE_LIST[recipeindex].update({'RecipeIngredients':ingredients})
        RECIPE_LIST[recipeindex].update({'RecipeMethod':method})
        return RECIPE_LIST

    def delete_recipe(self, recipeindex):
        """This method deletes a recipe"""
        self.recipeindex = recipeindex
        RECIPE_LIST.remove(RECIPE_LIST[recipeindex])
        return RECIPE_LIST
