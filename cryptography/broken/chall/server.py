from Crypto.Util.number import *
from secret import FLAG

FLAG = bytes_to_long(FLAG)
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
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    
    print(f"m: {pow(FLAG, e, n)}")
    print(f"n: {hex(n)}")
    print(f"p: {remove_partial(p)}")
    