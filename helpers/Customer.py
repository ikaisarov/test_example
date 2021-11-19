from helpers.RandomData import *


class Customer:

    def __init__(self, email=generate_random_email(), firstname='Сергей', lastname='Иванов', password=generate_alphanum_random_string(10),
                 birthday=str(random.randint(1, 5)), birthmonth="Февраль", birthyear= str(random.randint(1980, 2000))):
        self._email = email
        self._firstname = firstname
        self._lastname = lastname
        self._password = password
        self._birthday = birthday
        self._birthmonth = birthmonth
        self._birthyear = birthyear