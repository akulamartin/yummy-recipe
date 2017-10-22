#!/usr/bin/env python
import unittest

from app import app


class TestApp(unittest.TestCase):
 """This tests the initialization"""
def setUp(self):
        self.app.config['DEBUG']=False
def test_links(self):                
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
       unittest.main()
