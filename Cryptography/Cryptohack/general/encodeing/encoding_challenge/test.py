txt = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_45559noq}"
def rot13(s):
    return ''.join([chr((ord(c) - 97 + 13) % 26 + 97) if c.islower() else chr((ord(c) - 65 + 13) % 26 + 65) if c.isupper() else c for c in s])
print(rot13(txt))
