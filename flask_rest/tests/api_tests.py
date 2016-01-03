#!/usr/bin/env python3
import unittest
from api import api

class APITests(unittest.TestCase):
    def setUp(self):
        self.app = api.app.test_client()

    def tearDown(self):
        pass

    def test_conn(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)

if __name__ == '__main__':
    unittest.main()