from Crypto.Util.number import *
from sympy import *
from random import *
from secret import flag

def src_generate():
    q = getStrongPrime(512)
    p = prevprime(q)
    a = (p-1) // q
    h = randint(2, q - p)
    g = h**a % p
    return (p, q, g)

def priv_gen(q):
    x = getStrongPrime(512)
    while q < x:
        x = getStrongPrime(512)
    return x

def pub_gen(src):
    g, x, p = src
    y = g**x % p
    return y

def msg_enc(x, m):
    e = 65537
    c = bytes_to_long(m) ** e % x
    return c

def signature_gen(src):
    m, p, q, g, x = src
    H = msg_enc(x, m)
    k = randint(1,  q - p)
    r = g**k % p % q
    s = ((H + x * r) * pow(k, -1, q)) % q
    return (r, s, H)

def verification(src):
    r, s, H, p, q, g, y = src
    w = pow(s, -1, q)
    u1 = (H * w) % q
    u2 = (r * w) % q 
    v = (((pow(g, u1, p) * pow(y, u2, p)) % p) % q)
    return v == r

def write(data):
    with open("output.txt", "w") as file:
        file.write(str(data))

def main():
    m = flag
    p, q, g = src_generate()
    x = priv_gen(q)
    y = pub_gen((g, x, p))
    r, s, H = signature_gen((m, p, q, g, x))

    if verification((r, s, H, p, q, g, y)):
        write((p, r, s, H))
    else:
        print('Invalid Signature')

if __name__ == "__main__":
    main()