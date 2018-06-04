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
python genlicense.py key.pem 12:34:56:78:AB license.bin
```

Checking the generated license file:

```bash
python checklicense.py public.pem license.bin
```