import binascii
filename = 'Malware.zip'
with open(filename, 'rb') as f:
    content = f.read()
with open('hexData.hex', 'wb') as hexfile:
    hexfile.write(binascii.hexlify(content))