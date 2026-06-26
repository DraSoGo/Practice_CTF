c = 'TNURET_VYL_^SSRYh^YhG[V^Yh_CCGJ'
f = 'cyberchan{'
for i in range(len(f)):
    print(chr(ord(f[i]) ^ ord(c[i])), end=' ')
k = '7'
print()
for i in range(len(c)):
    print(chr(ord(k[0]) ^ ord(c[i])), end='')