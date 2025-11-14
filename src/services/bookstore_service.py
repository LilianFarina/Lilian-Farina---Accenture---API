from src.api_client import APIClient


class BookstoreService:
def __init__(self, base_url):
self.client = APIClient(base_url)


# Account endpoints
def create_user(self, username, password):
path = '/Account/v1/User'
payload = { 'userName': username, 'password': password }
return self.client.post(path, json=payload)


def generate_token(self, username, password):
path = '/Account/v1/GenerateToken'
payload = { 'userName': username, 'password': password }
return self.client.post(path, json=payload)


def is_authorized(self):
path = '/Account/v1/Authorized'
return self.client.get(path)


def get_user(self, user_id):
path = f'/Account/v1/User/{user_id}'
return self.client.get(path)


# Bookstore endpoints
def list_books(self):
path = '/BookStore/v1/Books'
return self.client.get(path)


def add_books_to_user(self, user_id, isbns, token=None):
path = '/BookStore/v1/Books'
payload = {
'userId': user_id,
'collectionOfIsbns': [{'isbn': isbn} for isbn in isbns]
}
headers = None
if token:
headers = { 'Authorization': f'Bearer {token}' }
return self.client.post(path, json=payload, headers=headers)
