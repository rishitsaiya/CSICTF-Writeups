from Crypto.Util.number import inverse
import binascii

e = 42667
c = 32949
n = 64741

# From factordb

p = 101
q = 641

phi = (p-1) * (q-1)

d = inverse(e,phi)
m = pow(c,d,n)

print (m)
