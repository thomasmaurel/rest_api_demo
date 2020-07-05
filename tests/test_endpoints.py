import json
import os
import unittest
from rest_api_demo.database import db
from rest_api_demo import app


class EndpointTest(unittest.TestCase):
    """Setup test"""

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()


    """Basic test case for testing creation of a new blog category"""

    def test_post(self):
        input = {
            'id': 5,
            'name': 'banana'
        }
        response = self.app.post('http://localhost:8888/api/blog/categories/',
                                 data=json.dumps(input),
                                 content_type='application/json')
        self.assertEqual(201, response.status_code)
        response2 = self.app.get('http://localhost:8888/api/blog/categories/5')
        self.assertEqual(200, response2.status_code)
        response3 = self.app.delete('http://localhost:8888/api/blog/categories/5')
        self.assertEqual(204, response3.status_code)
        results = json.loads(response2.data.decode('utf-8'))
        self.assertEqual(results.get('id'), 5)
        self.assertEqual(results.get('name'), 'banana')


    """Basic test case for testing retrieving of blog categorie"""

    def test_get_categorie(self):
        response = self.app.get('http://localhost:8888/api/blog/categories/1')
        self.assertEqual(200, response.status_code)
        results = json.loads(response.data.decode('utf-8'))
        self.assertEqual(results.get('id'), 1)
        self.assertEqual(results.get('name'), 'Sci-Fi')


    """Basic test case for retrieving a list of blog categories"""

    def test_get_categories(self):
        response = self.app.get('http://localhost:8888/api/blog/categories/')
        self.assertEqual(200, response.status_code)
        results = json.loads(response.data.decode('utf-8'))
        self.assertEqual(3,len(results))

    """Basic test case for deleting a blog categorie"""

    def test_delete_category(self):
        input = {
            'id': 6,
            'name': 'apple'
        }
        response = self.app.post('http://localhost:8888/api/blog/categories/',
                                 data=json.dumps(input),
                                 content_type='application/json')
        self.assertEqual(201, response.status_code)
        response2 = self.app.delete('http://localhost:8888/api/blog/categories/6')
        self.assertEqual(204, response2.status_code)


    """Basic test case for renaming a blog categorie"""

    def test_put_category(self):
        input = {
            'id': 7,
            'name': 'pear'
        }
        response = self.app.post('http://localhost:8888/api/blog/categories/',
                                 data=json.dumps(input),
                                 content_type='application/json')
        self.assertEqual(201, response.status_code)
        input2 = {
            'id': 7,
            'name': 'kiwi'
        }
        response2 = self.app.put('http://localhost:8888/api/blog/categories/7',
                                 data=json.dumps(input2),
                                 content_type='application/json')
        self.assertEqual(204, response2.status_code)
        response3 = self.app.get('http://localhost:8888/api/blog/categories/7')
        self.assertEqual(200, response3.status_code)
        results = json.loads(response3.data.decode('utf-8'))
        self.assertEqual(results.get('id'), 7)
        self.assertEqual(results.get('name'), 'kiwi')
        response4 = self.app.delete('http://localhost:8888/api/blog/categories/7')
        self.assertEqual(204, response4.status_code)


if __name__ == '__main__':
    unittest.main()