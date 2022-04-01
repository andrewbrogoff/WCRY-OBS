#!/usr/bin/python3
import base64
from sys import argv
 
def main():
    filename = argv[1]
    output_file = argv[2]
    var_name = argv[3]
    with open(filename, 'rb') as imagef:
        encoded_string = base64.b64encode(imagef.read())
        # print(encoded_string)
        with open(output_file, 'w') as binaryf:
                binaryf.write(var_name + ' = ' +  str(encoded_string))
                # binaryf.write(encoded_string)
                # binaryf.write('\'')

if __name__ == "__main__":
    main()