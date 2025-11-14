from src.utils.helpers import random_user


def before_all(context):
context.base_url = "https://demoqa.com"
context.user = random_user()
