import math
cypher_txt = "egqlvtjic{mv3hw3vrf_4xk4es_l0yoj}"
header = "cyberchan"
for i in range(len(header)):
    print(chr(int((ord(cypher_txt[i])-ord(header[i]))%26)+ord('a')),end = '')
print()

key = 'cipher'
key_idx = 0
for i in range(len(cypher_txt)):
    char = cypher_txt[i]
    if char.isalpha():
        c_val = ord(char) - ord('a')
        k_val = ord(key[key_idx % len(key)]) - ord('a')
        p_val = (c_val - k_val) % 26
        print(chr(p_val + ord('a')), end='')
        key_idx += 1
    else:
        print(char,end = '')

print()