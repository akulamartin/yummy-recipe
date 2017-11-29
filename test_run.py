"""This module performs tests"""
import unittest
import run

from app.classes.category import Category
from app.classes.recipe import Recipe
from app.classes.User import User


class TestUser(unittest.TestCase):
    """This class tests the user class"""

    def setUp(self):
        self.theuser = User()

    def test_login_user(self):
        """This method tests the user login"""
        result = self.theuser.login('martin@gmail.com', 'martin')
        self.assertNotEqual(result, None)

    def test_register_user(self):
        """The method tests user registration"""
        result = self.theuser.register(
            'martin', 'akula', 'martin@gmail.com', 'martin')
        self.assertNotEqual(result, None)


class TestCategory(unittest.TestCase):
    """This class tests the category class"""

    def setUp(self):
        self.category = Category()

    def test_add_category(self):
        """This method tests adding of categories"""
        self.assertRaises(
            RuntimeError, self.category.add_category, "Categoryname")

    def test_delete_category(self):
        """This method tests deleting of a category name"""
        self.assertRaises(IndexError, self.category.delete_category, 0)

    def test_edit_category(self):
        """This method tests editing of a categor name"""
        self.assertRaises(
            IndexError, self.category.edit_category, "Categoryname", 0)


class TestRecipe(unittest.TestCase):
    """This class tests the recipe class"""

    def setUp(self):
        self.rep = Recipe()

    def test_add_recipe(self):
        """This method tests adding of recipes"""
        self.assertRaises(RuntimeError, self.rep.add_recipe,
                          "Categoryname", "Recipename", "Ingredient", "Method")

    def test_edit_recipe(self):
        """This method tests editing of a categor name"""
        self.assertRaises(IndexError, self.rep.edit_recipe,
                          0, "recipename", "ingredients", "method")

    def test_delete_recipe(self):
        """This method tests editing of a categor name"""
        self.assertRaises(IndexError, self.rep.delete_recipe, 0)


class TestView(unittest.TestCase):
    """This class tests the view"""

    def setUp(self):
        run.APP.testing = True
        self.app = run.APP.test_client()

    def test_add_category(self):
        """This method tests addition of categories"""
        result = self.app.post(
            '/addCategories', data=str("Categoryname"), follow_redirects=True)
        self.assertNotEqual(result, None)

    def test_delete_category(self):
        """This method tests addition of categories"""
        result = self.app.post('/removeCategories', follow_redirects=True)
        self.assertNotEqual(result, None)

    def test_edit_category(self):
        """This method tests addition of categories"""
        result = self.app.post('/changeCategoryName/x/0',
                               follow_redirects=True)
        self.assertNotEqual(result, None)


class TestViewlinks(unittest.TestCase):
    """This class tests the view links"""

    def setUp(self):
        run.APP.testing = True
        self.app = run.APP.test_client()

    def test_login_link(self):
        """This method tests the route of the root"""
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_logout_link(self):
        """This method tests the route of the logout link"""
        result = self.app.get('/logout')
        self.assertEqual(result.status_code, 302)

    def test_register_link(self):
        """This method tests the route of the register link"""
        result = self.app.get('/Register')
        self.assertEqual(result.status_code, 200)

    def test_addcategories_link(self):
        """This method tests the route of the addcategories link"""
        result = self.app.get('/addCategories')
        self.assertEqual(result.status_code, 200)

    def test_removecategories_link(self):
        """This method tests the route of the removecategories link"""
        result = self.app.get('/removeCategories')
        self.assertEqual(result.status_code, 404)


if __name__ == '__main__':
    unittest.main()
