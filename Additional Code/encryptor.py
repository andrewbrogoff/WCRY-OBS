# import required module
from cryptography.fernet import Fernet

with open('key', 'rb') as key_file:
    key = key_file.read()
# using the key
fernet = Fernet(key)

# opening the encrypted file
with open('Wannacry Prank.py', 'rb') as file:
    original = file.read()

encrypted = fernet.encrypt(original)



# opening the file in write mode and
# writing the encrypted data
with open('Wannacry Prank.py.enc', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
