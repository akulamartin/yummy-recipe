"""This module performs tests"""
import unittest
import run
from app.classes.category import Category
from app.classes.recipe import Recipe
from app.classes.User import User

class TestCategory(unittest.TestCase):
    """This class tests the category class"""
    def setUp(self):
        self.category = Category()

    def test_category_instance(self):
        """This method tests the category instance"""
        cat = Category()
        self.assertEqual(isinstance(cat, Category), True)

    def test_add_category_at_runtime(self):
        """This method tests the runtime error"""
        cat = Category()
        self.assertRaises(RuntimeError, cat.add_category, "Categoryname")

    def test_delete_category(self):
        """This method tests deleting of a category name"""
        cat = Category()
        self.assertRaises(IndexError, cat.delete_category, 0)

    def test_edit_category(self):
        """This method tests editing of a categor name"""
        cat = Category()
        self.assertRaises(TypeError, cat.edit_category, 0)

class TestRecipe(unittest.TestCase):
    """This class tests the recipe class"""
    def setUp(self):
        self.recipe = Recipe()

    def test_recipe_instance(self):
        """This method tests the recipe instance"""
        rep = Recipe()
        self.assertEqual(isinstance(rep, Recipe), True)

    def test_add_recipe_at_runtime(self):
        """This method tests the runtime error """
        rep = Recipe()
        self.assertRaises(RuntimeError, rep.add_recipe,
                          "Categoryname", "Recipename", "Ingredient", "Method")

    def test_edit_recipe_type_error(self):
        """This method tests the editing of a recipe"""
        rep = Recipe()
        self.assertRaises(TypeError, rep.edit_recipe, 0)

    def test_delete_recipe_index_error(self):
        """This method tests the deletion of a recipe"""
        rep = Recipe()
        self.assertRaises(IndexError, rep.delete_recipe, 0)

class TestUser(unittest.TestCase):
    """This class tests the user class"""
    def setUp(self):
        self.user = User()

    def test_user_instance(self):
        """This method tests the user instance"""
        user = User()
        self.assertEqual(isinstance(user, User), True)

    def test_login_user(self):
        """This method tests the user login"""
        user = User()
        result = user.login('martin@gmail.com', 'martin')
        self.assertNotEqual(result, None)

    def test_register_user(self):
        """The method tests user registration"""
        user = User()
        result = user.register('martin', 'akula', 'martin@gmail.com', 'martin')
        self.assertNotEqual(result, None)

class TestApp(unittest.TestCase):
    """This class tests the application"""
    def setUp(self):
        run.APP.testing = True
        self.app = run.APP.test_client()

    def test_login_link(self):
        """This method tests the route of the root"""
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_logout_link(self):
        """This method tests the route of the root"""
        result = self.app.get('/logout')
        self.assertEqual(result.status_code, 302)

    def test_register_link(self):
        """This method tests the route of the root"""
        result = self.app.get('/Register')
        self.assertEqual(result.status_code, 200)

    def test_addcategories_link(self):
        """This method tests the route of the root"""
        result = self.app.get('/addCategories')
        self.assertEqual(result.status_code, 200)

    def test_removecategories_link(self):
        """This method tests the route of the root"""
        result = self.app.get('/removeCategories')
        self.assertEqual(result.status_code, 404)

    def test_editcategories_link(self):
        """This method tests the route of the root"""
        result = self.app.get('/changeCategoryName')
        self.assertEqual(result.status_code, 404)

    def test_recipe_link(self):
        """This method tests the route of the root"""
        result = self.app.get('/recipe')
        self.assertEqual(result.status_code, 404)

    def test_editrecipe_link(self):
        """This method tests the route of the root"""
        result = self.app.get('/editrecipe')
        self.assertEqual(result.status_code, 404)

    def test_deleterecipe_link(self):
        """This method tests the route of the root"""
        result = self.app.get('/deleterecipe')
        self.assertEqual(result.status_code, 404)

if __name__ == '__main__':
    unittest.main()
