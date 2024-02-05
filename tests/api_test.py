import unittest
import sys
import os
import json  # Add missing import statement # Add the parent directory to the sys.path
from ..api.v1.app import app
from flask import json

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_status(self):
        response = self.app.get('/api/v1/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"status": "OK"})

if __name__ == '__main__':
    unittest.main()