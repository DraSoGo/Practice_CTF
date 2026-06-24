c = 'label'
k = 13
for i in c:
    print(chr(ord(i)^k), end='')
# result = ''.join(chr(ord(char) ^ k) for char in c)
# print(result)