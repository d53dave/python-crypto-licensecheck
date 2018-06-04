import sys

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

def obtain_machine_specific_data():
    return '12:34:56:78:AB'

def verify_data(pubkey, input_file, data):
    with open(pubkey, 'r', encoding='utf-8') as pubkey_file:
        with open(input_file, 'rb') as in_file:
            key = RSA.importKey(pubkey_file.read())
            h = SHA256.new(data.encode('utf-8'))

            try:
                pkcs1_15.new(key).verify(h, in_file.read())
                return True
            except (ValueError, TypeError):
                pass
            
            return False

if __name__ == '__main__':
    pubkey_file = sys.argv[1]
    license_file = sys.argv[2]

    valid = verify_data(pubkey_file, license_file, obtain_machine_specific_data())
    
    print('Valid licence') if valid else print('Invalid License') 