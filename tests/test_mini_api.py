import unittest
import json
from src.mini_api import app, fake_database

class TestAPIEndpoints(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        # Reset fake database after each test
        fake_database['email'] = []

    def test_get_message(self):
        response = self.app.get('/api')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Hello, world!')

    def test_get_all_users_empty(self):
        response = self.app.get('/api/all_users')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, {'email': []})

    def test_add_user_success(self):
        user_data = {'email': 'test@example.com'}
        response = self.app.post('/api/add_user', json=user_data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'User added successfully')
        self.assertIn('test@example.com', fake_database['email'])

    def test_add_user_already_exists(self):
        # Add a user to the fake database
        fake_database['email'].append('existing_user@example.com')

        user_data = {'email': 'existing_user@example.com'}
        response = self.app.post('/api/add_user', json=user_data)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['message'], 'User already exist')
        self.assertEqual(len(fake_database['email']), 1)  # No duplicate user added

if __name__ == '__main__':
    unittest.main()
