#!/usr/bin/env python
import unittest

from app import app


class TestApp(unittest.TestCase):
 """This tests the initialisation"""
def setUp(self):
        self.app.config['DEBUG']=False
def test_links():                
    pass

if __name__ == '__main__':
       unittest.main()
