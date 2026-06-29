from Crypto.PublicKey import RSA
f = open('transparency.pem', 'r')
pubkey = RSA.import_key(f.read())
print(pubkey.n)
