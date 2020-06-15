import string
from random import randint
import random
from cryptography.fernet import Fernet
key = Fernet.generate_key()
file = open('key.key', 'wb')
file.write(key)
file.close()

upper_alphabet = string.ascii_uppercase
lower_alphabet = string.ascii_lowercase
special_character = ['!', '@', '$', '&', '*', ':', ';', '.', '?']
pass_list = []


class Password:
    def __init__(self, password_length):
        self.password_length = password_length
        for i in range(password_length):
            comp_1 = random.choice(lower_alphabet)
            comp_2 = random.choice(upper_alphabet)
            comp_3 = randint(0, 9)
            comp_4 = random.choice(special_character)
            value = str(random.choice([comp_1, comp_2, comp_3, comp_4]))
            pass_list.append(value)
        password = ''.join([str(elem) for elem in pass_list])
        self.generate_password = password

    def encryption(self):
        self.generate_password
        message = self.generate_password.encode()
        f = Fernet(key)
        encrypted = f.encrypt(message)
        return encrypted


password_length = int(input(f'Enter password length: '))
if password_length >= 8:
    obj = Password(password_length)
    hash_value = obj.encryption()
    file = open('password_hash.key', 'wb')
    file.write(hash_value)
    file.close()
    print(f"The generated password is: {obj.generate_password}\n")
    print(f'note:- Decrypt key saved as key.key\nPassword hash value saved as password_hash.key')
else:
    print('Enter minimum length 8')




