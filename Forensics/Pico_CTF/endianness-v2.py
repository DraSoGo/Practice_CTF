def get_hex(filename):
    with open(filename, 'rb') as f:
        hex_data = f.read().hex()
        return hex_data


result = get_hex('endianness-v2')
new_hex = ''
for i in range(0, len(result), 8):
    hex = result[i:i+8]
    tmp_hex = ''
    for j in range(len(hex)-1, -1, -2):
        tmp_hex += hex[j-1] + hex[j]
    new_hex += tmp_hex
    # print(f'{hex} -> {tmp_hex}')
print(new_hex)