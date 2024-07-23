from Crypto.Util.number import *
from sympy import *
from random import *
from secret import flag

def src_generate():
    q = getStrongPrime(2048)
    p = getStrongPrime(2048)
    while(p > q):
        p = getStrongPrime(2048)
    a = (p-1) // q
    h = randint(2, q - p)
    g = h**a % p
    return (p, q, g)

def random_number():
    return getStrongPrime(512)

def priv_gen(m):
    x = m
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
    m, p, q, g, x, k = src
    H = bytes_to_long(m)
    r = g**k % p % q
    s = ((H + x * r) * pow(k, -1, q)) % q
    return (r, s, H, q)

def verification(src):
    r, s, H, p, q, g, y = src
    w = pow(s, -1, q)
    u1 = (H * w) % q
    u2 = (r * w) % q 
    v = (((pow(g, u1, p) * pow(y, u2, p)) % p) % q)
    return v == r

def message_signing(src):
    message = input('\nInput Message : ')
    p, q, g, x, rand = src
    print(signature_gen((message.encode(), p, q, g, x, rand)))

def main():
    m = flag
    p, q, g = src_generate()
    x = priv_gen(bytes_to_long(m))
    rand = random_number()

    loop = True
    while loop:
        print('\n1. Generate Signature\n0. Exit\n')
        user_input = input("Your Input : ")

        match user_input:
            case '1':
                message_signing((p, q, g, x, rand))
            case '0':
                loop = False
            case _:
                print("Invalid input. Please enter 1 or 0.")

if __name__ == "__main__":
    main()