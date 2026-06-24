c1_hex = "5a75ee1800245c4db66b7d1c1a043c0bb12fd5fa730ee9ddd12b5d985043bb4c"
c2_hex = "6d64e50e522e470cb2657c5b4f162d0bb90288ef6f71b5cbfd3c0fcb5103e25f"
p2_text = "This is just a normal message, n"

c1 = bytes.fromhex(c1_hex)
c2 = bytes.fromhex(c2_hex)
p2 = p2_text.encode()

m1_bytes = bytes([b1 ^ b2 ^ b3 for b1, b2, b3 in zip(c1, c2, p2)])
print(m1_bytes)