# import required module
from cryptography.fernet import Fernet

with open('localkey', 'rb') as key_file:
    key = key_file.read()
# using the key
fernet = Fernet(key)

# opening the encrypted file
with open('onlinekey', 'rb') as enc_file:
    encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
with open('onlinekey.dec', 'wb') as dec_file:
    dec_file.write(decrypted)