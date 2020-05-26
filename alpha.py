import string
from random import randint
import random


upper_alphabet = string.ascii_uppercase
lower_alphabet = string.ascii_lowercase
special_character = ['!', '@', '$', '&', '*', ':', ';', '.', '?']


def number(password_length):
    print(f'Your password:\n{random.choice(lower_alphabet)}{random.choice(special_character)}', end='')
    for i in range(password_length - 4):
        value = randint(0, 9)
        print(value, end='')
    print(f'{random.choice(upper_alphabet)}{random.choice(special_character)}', end='')


password_length = int(input(f'\nNB:-minimum length is 8\nEnter password length: '))
if password_length >= 8:
    number(password_length)
else:
    print('Enter minimum length 8')

