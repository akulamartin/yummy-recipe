#!/usr/bin/env python
import unittest

from app import app


class TestApp(unittest.TestCase):
 """This tests the initialisation"""
def setUp(self):
        app.config['DEBUG']=True
                

if __name__ == '__main__':
       unittest.main()
