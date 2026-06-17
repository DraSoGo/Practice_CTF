text = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
raw = bytes.fromhex(text)
print(raw)

def xor(data, key):
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])
    # return bytes([x ^ y for x, y in zip(a, b)])

for i in range(256):
    key = bytes([i])
    result = xor(raw, key)
    print(f'{i:02x}: {result.decode('utf-8', errors='ignore')}')