# import required module
from cryptography.fernet import Fernet

# key generation
key = Fernet.generate_key()

# string the key in a file
with open('localkey.key', 'wb') as filekey:
    filekey.write(key)

# opening the key
with open('localkey.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

# key generation
onlinekey = Fernet.generate_key()

# string the key in a file
with open('bckup_onlinekey.key', 'wb') as filekey:
    filekey.write(onlinekey)

# opening the original file to encrypt
with open('bckup_onlinekey.key', 'rb') as file:
    original = file.read()

# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and
# writing the encrypted data
with open('onlinekey.key', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)