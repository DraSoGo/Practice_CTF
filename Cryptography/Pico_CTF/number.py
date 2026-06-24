mapping = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
c = [16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]
def decode(c):
    return ''.join([list(mapping.keys())[list(mapping.values()).index(i)] for i in c])
print(decode(c))