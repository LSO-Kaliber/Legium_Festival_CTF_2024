from Crypto.Util.number import *
from secret import flag

value_dict = {0 : 5, 1 : 6, 2 : 7, 3 : 8, 4 : 9}
number_dict = {v: k for k, v in value_dict.items()}

def source(flag):
    p = getStrongPrime(512)
    q = getStrongPrime(512)
    pt = bytes_to_long(flag)
    e = 0x10001
    n = p * q
    return [p, q, n, e, pt]

def encrypt(source):
    a, b, c, d, e = source
    ct = pow(e, d, c)
    ext = (c ** 2) + ((a * 2) + (b * 2))
    return [c, d, ct, ext]

def encrypt_ext(source):
    a, b, c, d = source
    ct2 = ""
    for data in str(d):
        if (int(data) <= 4): ct2 += str(rot_1(int(data)))
        if (int(data) >= 5): ct2 += str(rot_2(int(data)))
    ct2 = int(ct2)
    return [a, b, c, ct2]

def rot_1(val):
    return value_dict.get(val, val)

def rot_2(val):
    return number_dict.get(val, val)

def write(res):
    file = open("output.txt", "w")
    file.write(str(res))
    file.close

def run():
    src_1 = source(flag)
    src_2 = encrypt(src_1)
    src_3 = encrypt_ext(src_2)
    write(src_3)

if __name__ == "__main__":
    run()