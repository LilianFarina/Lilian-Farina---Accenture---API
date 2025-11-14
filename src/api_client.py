import requests


class APIClient:
def __init__(self, base_url):
self.base_url = base_url.rstrip('/')
self.session = requests.Session()


def post(self, path, json=None, headers=None):
url = f"{self.base_url}{path}"
r = self.session.post(url, json=json, headers=headers)
r.raise_for_status()
return r.json()


def get(self, path, params=None, headers=None):
url = f"{self.base_url}{path}"
r = self.session.get(url, params=params, headers=headers)
r.raise_for_status()
return r.json()
