from Crypto.Util.number import *
from secret import flag, nbit

p = getPrime(nbit)
q = getPrime(nbit)

assert p != q

N = p * q

for i in range(1000):
    if GCD(flag, i) == 1:
        N *= i
        
cp = pow(flag, 65537, N)
print(f"cp = {cp}")