from sage.all import *
from Crypto.Util.number import *

N = 0x98ec72fee2a089e0b5278c0f809aebbce0a3545cf1b901a92686218825cdbec99d1a232e61531b307c1702db6af437123aafe08c5056ee5b4ca9d53b35f9199f22011543d0b995b592c53ade1f2c48d5d097317f8705fbd04b0d396fd1120664aecce1d41050c398ab050bc7d2f428be61eec0ca4ddd9e49072cf8830de2c62d

# https://github.com/jvdsn/crypto-attacks/blob/master/attacks/factorization/coppersmith.py
import sys
import os
path = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.realpath(os.path.abspath(__file__)))))
if sys.path[1] != path:
    sys.path.insert(1, path)
from crypto_attacks.shared.partial_integer import PartialInteger
from crypto_attacks.attacks.factorization.coppersmith import factorize_p

p = "aa437db77b4566a7678a2691cb4ec184522?????????ded9c8f3ba87f8def78d89?????????52a1e06e5039aa9ce4ca85a6afcc627a6667???????5484dfc357"
p = PartialInteger.parse_be(p, 16)
p, q = factorize_p(N, p, m=6, t=2)
print(f"{p = }")
print(f"{q = }")
m = 30688422491999425135495180913535905832237802753908754613708118839069187892109873378098557502137859123810748428193915457900195834239641495190156666922935133351552592776351007641529214315465314422348562051010487912698960454466125373669665748594331941147947029305916210441419067033189643601168207547880327711557

n = p * q
phi = (p - 1) * (q - 1)
d = inverse(65537, phi)
print(long_to_bytes(pow(m, d, n)))