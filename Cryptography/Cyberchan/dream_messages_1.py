import math
cypher_txt = "fpfedfyen{h1j3e3v3_1s_nu0b3r}"
header = "cyberchan"
for i in range(len(header)):
    print(chr(int((ord(cypher_txt[i])-ord(header[i]))%26)+ord('a')),end = '')
print()

key = 'dream'
key_idx = 0
for i in range(len(cypher_txt)):
    char = cypher_txt[i]
    if char.isalpha():
        c_val = ord(char) - ord('a')
        k_val = ord(key[key_idx % len(key)]) - ord('a')
        print(key_idx)
        p_val = (c_val - k_val) % 26
        print(chr(p_val + ord('a')), end='')
        key_idx += 1
    else:
        print(char,end = '')

print()
