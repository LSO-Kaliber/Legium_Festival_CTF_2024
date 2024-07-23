from Crypto.Util.number import *
from secret import FLAG

FLAG1 = bytes_to_long(FLAG[:31])
FLAG2 = bytes_to_long(FLAG[31:])
def generate_prime():
    p = getPrime(512)
    q = getPrime(512)
    while p == q:
        p = getPrime(512)
    
    return p, q, 65537

def remove_partial(p: int):
    p = hex(p)[2:]
    result = (
        p[:35] + "?" * 9 +
        p[44:66] + "?" * 9 +
        p[75:111] + "?" * 7 +
        p[118:]
    )
    return result

if "__main__" == __name__:
    p, q, e = generate_prime()
    n = p * q
    
    r = getStrongPrime(1024)
    
    print(f"m1: {pow(FLAG1, e, n)}")
    print(f"m2: {pow(FLAG2, e, r)}")
    print(f"n1: {hex(n)}")
    print(f"n2: {r - p}")
    print(f"p: {remove_partial(p)}")
    