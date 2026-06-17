import string

score_dict = {}

def get_english_score(text):
    return sum(1 for char in text if char in string.ascii_letters or char == ' ')
def xor(data: bytes, key: int):
    return bytes([b ^ key for b in data])

with open('/home/drasogo/DraSoGo/Practice_CTF/Cryptography/Cryptopals/01_04.txt') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
    try:
        data = bytes.fromhex(line)
    except ValueError:
        continue
    for key in range(256):
        result = xor(data, key)
        plaintext = result.decode('utf-8', errors='ignore')
        score = get_english_score(plaintext)
        score_dict[plaintext] = score
sorted_scores = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)
print(f"Top 5: {sorted_scores[:5]}")