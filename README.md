# python-crypto-licensecheck

This tool encrypts a given input string using a private key and generates a file
that can be transmitted and verified on clients using the corresponding public key.

## Requirements

Tested with `Python 3.6.4` and `pycryptodome` for the crypto primitives, so make sure to
`pip install pycryptodome` before trying the code.

## Preparation

Generate a key pair, RSA 2048

```bash
openssl genrsa -out key.pem 2048
```

and

```bash
openssl rsa -in key.pem -outform PEM -pubout -out public.pem
```

## Usage

Generating a license file (read: signed hash of input string):

```bash
python genlicense.py path/to/key.pem <input string> path/to/output_file.bin
```

Checking the generated license file:

```bash
python checklicense.py path/to/public.pem path/to/output_file.bin
```

`checklicense.py` is expected to generate the license content based on data
from the machine it is deployed on. It will use this data and check against
the signature produced by `genlicense.py`. Examples for such data would be
hardware fingerprints or Mac-adresses, maybe in combination with unique user data.