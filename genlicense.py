import sys

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

def sign_data(key, data, output_file):
    with open(key, 'r', encoding='utf-8') as keyFile:
        rsakey = RSA.importKey(keyFile.read())
        signer = pkcs1_15.new(rsakey)
        digest = SHA256.new(data.encode('utf-8'))
        with open(output_file, 'wb') as out:
             out.write(signer.sign(digest))

if __name__ == '__main__':
    key_file = sys.argv[1]
    input_string = sys.argv[2]
    out_file = sys.argv[3]

    sign_data(key_file, input_string, out_file)
