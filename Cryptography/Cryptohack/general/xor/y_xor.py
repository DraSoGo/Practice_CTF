c = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
p1 = b'crypto{'
print(bytes([b ^ p1[i % len(p1)] for i, b in enumerate(c)]))
k = b'myXORkey'
p2 = bytes([b ^ k[i % len(k)] for i, b in enumerate(c)])
print(p2)
