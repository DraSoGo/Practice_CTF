import base64 as b64
def score_english(text_bytes):
    freq = {
        'a': 0.0817, 'b': 0.0149, 'c': 0.0278, 'd': 0.0425, 'e': 0.1270,
        'f': 0.0223, 'g': 0.0202, 'h': 0.0609, 'i': 0.0697, 'j': 0.0015,
        'k': 0.0077, 'l': 0.0403, 'm': 0.0241, 'n': 0.0675, 'o': 0.0751,
        'p': 0.0193, 'q': 0.0009, 'r': 0.0599, 's': 0.0633, 't': 0.0906,
        'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015, 'y': 0.0197,
        'z': 0.0007, ' ': 0.1300
    }
    score = 0
    for byte in text_bytes:
        ch = chr(byte).lower()
        if ch in freq:
            score += freq[ch]
        elif byte == 10 or byte == 13:
            score += 0.01
        elif 32 <= byte <= 126:
            score += 0.001
        else:
            score -= 10
    return score

def hamming_distance(a, b):
    if isinstance(a, str):
        a = a.encode('utf-8')
    if isinstance(b, str):
        b = b.encode('utf-8')
    ham = []
    for c1, c2 in zip(a, b):
        ham.append(bin(c1 ^ c2).count('1'))
    return sum(ham)

def find_key(decoded):
    candidate_keysizes = []
    
    for keysize in range(2, 40):
        distances = []
        num_blocks = len(decoded) // keysize
        if num_blocks < 2:
            continue
        for i in range(num_blocks - 1):
            b1 = decoded[i * keysize : (i + 1) * keysize]
            b2 = decoded[(i + 1) * keysize : (i + 2) * keysize]
            distances.append(hamming_distance(b1, b2) / keysize)
        avg_dist = sum(distances) / len(distances)
        candidate_keysizes.append((avg_dist, keysize))
    candidate_keysizes.sort()
    return candidate_keysizes[0][1]

def find_byte(block):
    best_score = float('-inf')
    best_byte = None
    for byte in range(256):
        decrypted = bytes([b ^ byte for b in block])
        score = score_english(decrypted)
        if score > best_score:
            best_score = score
            best_byte = byte
    return best_byte
def decrypt_repeating_key_xor(decoded, key):
    decrypted = b""
    for i in range(len(decoded)):
        decrypted += bytes([decoded[i] ^ key[i % len(key)]])
    return decrypted

with open('/home/drasogo/DraSoGo/Practice_CTF/Cryptography/Cryptopals/01_06.txt') as f:
    data = f.read().replace('\n', '')
    decoded = b64.b64decode(data)
print(hamming_distance("this is a test", "wokka wokka!!!"))
key_size = find_key(decoded)
print(key_size)
final_key = []
for i in range(key_size):
    block = decoded[i::key_size]
    byte = find_byte(block)
    final_key.append(byte)
print(final_key)
key_string = "".join(chr(b) for b in final_key)
print(key_string)

plain_text = decrypt_repeating_key_xor(decoded, final_key)
print(plain_text.decode("utf-8"))