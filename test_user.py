#!/usr/bin/env python
import unittest
from user import User
class  UserTest(unittest.TestCase):
        """This tests the initialisation"""
        def setUp(self):
            self.user=User()    

        def test_user_registration(self):
            """This tests for complete fields"""
            result=self.user.get_user_register("martin","akula","martin.akula@gmail.com","akulamartin","eat")
            self.assertEqual(1,result,"User registration successful")

        def test_empty_first_name_field(self):
            """Test for either empty field """
            result=self.user.get_user_register("","akula","martin.akula@gmail.com","akulamartin","eat")
            self.assertEqual(2,result,"Please fill in the first name field")

        def test_empty_second_name_field(self):
            """Test for either empty field """
            result=self.user.get_user_register("martin","","martin.akula@gmail.com","akulamartin","eat")
            self.assertEqual(2,result,"Fill in the second name field please")

        def test_empty_email_field(self):
            """Test for either empty field """
            result=self.user.get_user_register("martin","akula","","akulamartin","eat")
            self.assertEqual(2,result,"Fill in the email field please")

        def test_empty_user_name_field(self):
            """Test for either empty field """
            result=self.user.get_user_register("martin","akula","martin.akula@gmail.com","","eat")
            self.assertEqual(2,result,"Fill in the username field please")

        def test_empty_password_field(self):
            """Test for either empty field """
            result=self.user.get_user_register("martin","akula","martin.akula@gmail.com","akulamartin","")
            self.assertEqual(2,result,"Fill in the password field please")

       # def test_user_in_register(self):
        #    """Test username and password"""
         ##  result=self.user.get_user_register("martin","akula","martin.akula@gmail.com","akulamartin","eat")
           # self.assertEqual(3,result,"Fill in the password field please")            
           
if __name__=='__main__':
       unittest.main()
