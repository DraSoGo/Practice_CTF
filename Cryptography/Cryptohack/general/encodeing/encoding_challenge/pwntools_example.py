from pwn import * # pip install pwntools
from Crypto.Util.number import *
import json
import base64

def b64(b):
    return base64.b64decode(b).decode()

def hex(b):
    return bytes.fromhex(b).decode()

def utf8(b):
    p = ''
    for i in b:
        p += chr(i)
    return p

def rot13(s):
    return ''.join([chr((ord(c) - 97 + 13) % 26 + 97) if c.islower() else chr((ord(c) - 65 + 13) % 26 + 65) if c.isupper() else c for c in s])

def bigint(b):
    return bytes.fromhex(b[2:]).decode()

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

for i in range(1000):
    received = json_recv()
    
    print(f"Received type: {received["type"]}")
    print(f"Received encoded value: {received["encoded"]}")
    to_send = {"decoded": "null"}
    if received["type"] == "base64":
        to_send = {"decoded": b64(received["encoded"])}
    elif received["type"] == "hex":
        to_send = {"decoded": hex(received["encoded"])}
    elif received["type"] == "utf-8":
        to_send = {"decoded": utf8(received["encoded"])}
    elif received["type"] == "rot13":
        to_send = {"decoded": rot13(received["encoded"])}
    elif received["type"] == "bigint":
        to_send = {"decoded": bigint(received["encoded"])}
    print(f"Sending decoded value: {to_send["decoded"]}")
    json_send(to_send)
