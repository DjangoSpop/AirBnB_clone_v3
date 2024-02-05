import unittest
import sys
sys.path.insert(0, '..')
from flask import json
from api.v1.app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_status(self):
        response = self.app.get('/api/v1/status')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"status": "OK"})

if __name__ == '__main__':
    unittest.main()