"""This modue holds the htmls to render"""
from flask import render_template, session, flash, request, redirect, url_for
from app import APP
from .classes.User import User
from .classes.category import Category, CATEGORY_LIST
from .classes.recipe import Recipe, RECIPE_LIST

#This route is used to login the user
@APP.route('/', methods=['GET', 'POST'])
def login():
    """This function renders the index page"""
    error = None
    user = User()
    if request.method == 'POST':
        error = user.login(request.form['Email'], request.form['Password'])
        if not error:
            session['logged_in'] = True
            flash('You were logged in')
            return render_template('addcategories.html', category=CATEGORY_LIST, recipe=RECIPE_LIST)
    return render_template('login.html', error=error)

#This route is used to logout the user
@APP.route('/logout')
def logout():
    """This function is used to log out"""
    session.pop('logged_in', None)
    session.pop('firstname', None)
    session.pop('email', None)
    session.pop('password', None)
    flash('You were logged out')
    return redirect(url_for('login'))

#This route is used to register the user
@APP.route('/Register', methods=['GET', 'POST'])
def register_user():
    """This function is used to register a user"""
    error = None
    user = User()
    if request.method == 'POST':
        error = user.register(request.form['regfirstname'], request.form['reglastname'],
                              request.form['regEmail'], request.form['regPassword'])
        if not error:
            flash('You have been registered')
            return redirect(url_for('login'))
    return render_template('register.html', error=error)

#This route is used to add categories
@APP.route('/addCategories', methods=['GET', 'POST'])
def add_categories():
    """This function adds the category to the page page"""
    cat = Category()
    if request.method == 'POST':
        cat.add_category(request.form['getCategory'])
        flash('You have added a category')
        return render_template('addcategories.html', category=CATEGORY_LIST)
    return render_template('addcategories.html', category=CATEGORY_LIST)

#This route is used to remove categories
@APP.route('/removeCategories/<categoryname>/<int:categoryindex>', methods=['GET', 'POST'])
def remove_categories(categoryname, categoryindex):
    """This function adds the category to the page page"""
    cat = Category()
    cat.delete_category(categoryindex)
    RECIPE_LIST[:] = [d for d in RECIPE_LIST if d.get('Category') != categoryname]
    flash('You have removed a category')
    return render_template('addcategories.html', category=CATEGORY_LIST, recipe=RECIPE_LIST)

#This route is used to change the category name
@APP.route('/changeCategoryName/<categoryname>/<int:categoryindex>', methods=['GET', 'POST'])
def edit_categories(categoryname, categoryindex):
    """This function edits the category name"""
    cat = Category()
    if request.method == 'POST':
        cat.edit_category(request.form['changeCategory'], categoryindex)
        for rep in RECIPE_LIST:
            if rep['Category'] == categoryname:
                rep.update({'Category':request.form['changeCategory']})
        flash('You have changed the category name')
        return render_template('addcategories.html', category=CATEGORY_LIST, recipe=RECIPE_LIST)
    return render_template('changecategoryname.html', changename=categoryname,
                           category=CATEGORY_LIST, recipe=RECIPE_LIST, categoryindex=categoryindex)

#This route is used to add a recipe
@APP.route('/recipe/<rcategory>', methods=['GET', 'POST'])
def add_recipe(rcategory):
    """This function adds a recipe"""
    rep = Recipe()
    if request.method == 'POST':
        rep.add_recipe(
            rcategory, request.form['Recipename'],
            request.form['Recipeingredients'], request.form['Recipemethod'])
        flash('You have added a recipe')
        return render_template('addcategories.html', category=CATEGORY_LIST, recipe=RECIPE_LIST)
    return render_template('addrecipe.html',
                           category=CATEGORY_LIST, rcat=rcategory, recipe=RECIPE_LIST)

#This route is used to delete a recipe
@APP.route('/deleterecipe/<int:recipeindex>', methods=['GET', 'POST'])
def delete_recipe(recipeindex):
    """This function deletes a recipe"""
    rep = Recipe()
    rep.delete_recipe(recipeindex)
    flash('You have deleted a recipe')
    return render_template('addcategories.html', category=CATEGORY_LIST, recipe=RECIPE_LIST)

#This route is used to edit a recipe
@APP.route('/editrecipe/<int:recipeindex>', methods=['GET', 'POST'])
def edit_recipe(recipeindex):
    """This function edits a recipe"""
    rep = Recipe()
    if request.method == 'POST':
        rep.edit_recipe(
            recipeindex, request.form['Recipename'],
            request.form['Recipeingredients'], request.form['Recipemethod'])
        flash('You have edited a recipe')
        return render_template('addcategories.html', category=CATEGORY_LIST, recipe=RECIPE_LIST)
    return render_template('editrecipe.html', rindex=recipeindex,
                           recipe=RECIPE_LIST, category=CATEGORY_LIST)
