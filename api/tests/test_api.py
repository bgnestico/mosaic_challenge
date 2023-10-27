import requests
import unittest
import random


class TestBooksApi(unittest.TestCase):
    url = 'http://127.0.0.1:5000/'
    book_id = random.randint(10, 1000)

    def setUp(self):
        payload = {'id': self.book_id, 'title': 'title_setup', 'author': 'author_setup', 'publication_date': '07-07-22'}
        requests.post(self.url + 'books', json=payload)

    def test_get_all_books(self):
        response = requests.get(self.url + 'books')
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(data)

    def test_new_book_created(self):
        payload = {'id': self.book_id, 'title': 'title_{}'.format(self.book_id),
                   'author': 'author{}'.format(self.book_id), 'publication_date': '08-08-22'}
        response = requests.post(self.url+'books', json=payload)
        data = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'Book created')

        validate_get_response = requests.get(self.url + 'books/' + str(self.book_id))
        self.assertEqual(validate_get_response.status_code, 200)
        data = validate_get_response.json()
        self.assertEqual(data['id'], payload['id'])
        # requests.delete(self.url + 'books/' + str(self.book_id))

    def test_get_book_by_id(self):
        response = requests.get(self.url+'books/'+str(self.book_id))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['id'], self.book_id)
        self.assertEqual(data['title'], 'title_setup')
        self.assertEqual(data['author'], 'author_setup')
        self.assertEqual(data['publication_date'], '07-07-22')

    def test_modify_book(self):
        payload = {'id': self.book_id, 'title': 'title_mod', 'author': 'author_mod', 'publication_date': '08-08-20'}
        response = requests.put(self.url+'books/'+str(payload['id']), json=payload)
        self.assertEqual(response.status_code, 200)

        validate_get_response = requests.get(self.url + 'books/' + str(payload['id']))
        self.assertEqual(validate_get_response.status_code, 200)
        data = validate_get_response.json()
        self.assertEqual(data['id'], payload['id'])
        self.assertEqual(data['title'], payload['title'])
        self.assertEqual(data['author'], payload['author'])
        self.assertEqual(data['publication_date'], payload['publication_date'])

    def test_delete_book(self):
        response = requests.delete(self.url + 'books/' + str(self.book_id))
        self.assertEqual(response.status_code, 200)
        delete_data = response.json()
        print(delete_data)
        print(response)
        self.assertEqual(delete_data['message'], 'Book deleted successfully')

        validate_get_response = requests.get(self.url + 'books/' + str(self.book_id))
        self.assertEqual(validate_get_response.status_code, 404)
        get_data = validate_get_response.json()
        print(get_data)
        self.assertEqual(get_data['message'], 'Book not found')

    def tearDown(self):
        # requests.delete(self.url + 'books/' + str(self.book_id))
