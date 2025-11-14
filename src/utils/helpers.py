import random
import string
import os


from dotenv import load_dotenv
load_dotenv()




def random_string(n=8):
return ''.join(random.choices(string.ascii_letters + string.digits, k=n))




def random_user():
username = f'user_{random_string(8)}'
password = f'P@ss{random_string(8)}'
return {
'username': username,
'password': password
}
