import string
from random import randint
import random


upper_alphabet = string.ascii_uppercase
lower_alphabet = string.ascii_lowercase
special_character = ['!', '@', '$', '&', '*', ':', ';', '.', '?']


def generate(password_length):
    for i in range(password_length):
        comp_1 = random.choice(lower_alphabet)
        comp_2 = random.choice(upper_alphabet)
        comp_3 = randint(0, 9)
        comp_4 = random.choice(special_character)
        value = str(random.choice([comp_1, comp_2, comp_3, comp_4]))
        print(value, end='')
        


password_length = int(input(f'\nNB:-minimum length is 8\nEnter password length: '))
if password_length >= 8:
    generate(password_length)
else:
    print('Enter minimum length 8')


