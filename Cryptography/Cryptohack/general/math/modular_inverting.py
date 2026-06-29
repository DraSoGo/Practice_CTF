def extended_gcd(a, b):
    old_r, r = a, b
    old_p, p = 1, 0
    old_s, s = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_p, p = p, old_p - q * p
        old_s, s = s, old_s - q * s
    return old_r, old_p, old_s

a = 3
b = 13
r, p, s = extended_gcd(a, b)
print(r, p, s)