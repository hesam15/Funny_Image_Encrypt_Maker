import os.path
from EnDecryptor import Encrypter
from EnDecryptor import Decrypter

request = input('Do you want to Encrypt(E) or Decrypt(D)?: ')

path = input('Give me your image: ')

if os.path.isfile(path):
    if request.lower() == 'e' or request.lower() == 'encrypt':
        Encrypter.encrypt(path)
    elif request.lower() == 'd' or request.lower() == 'dencrypt':
        Decrypter.decrypter(path)
    else:
        print('Incorrect request')
else:
    print('Image path is incorrect')