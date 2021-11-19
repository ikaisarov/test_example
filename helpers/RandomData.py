import requests
import random
import string

def generate_random_email():
    return requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox').json()

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.sample(letters_and_digits, length))