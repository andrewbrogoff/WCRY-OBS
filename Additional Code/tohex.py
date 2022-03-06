import binascii
filename = 'Malware.zip'
with open(filename, 'rb') as f:
    content = f.read()
print(binascii.hexlify(content))