import ctypes
import struct

def deterministic_number(a1):
    return (a1 * a1 + 33 * a1 + 1337 + a1)

def generate_deterministic_integers(a1, a2, a3):
    for i in range(a2):
        struct.pack_into('I', a1, 4 * i, deterministic_number(i + a3))
    return a2

def hash_function(a1, a2, a3):
    for i in range(a2):
        val = struct.unpack_from('I', a1, 4 * i)[0] ^ 0x2A
        struct.pack_into('I', a3, 4 * i, val)
    return a2

def xor_arrays(a1, a2, a3, a4):
    for i in range(a4):
        val = struct.unpack_from('I', a1, 4 * i)[0] ^ struct.unpack_from('I', a2, 4 * i)[0]
        struct.pack_into('I', a3, 4 * i, val)
    return a4

def transform_integers(a1, a2):
    for i in range(a2):
        val = 3 * struct.unpack_from('I', a1, 4 * i)[0] + 7
        struct.pack_into('I', a1, 4 * i, val)
    return a2

def permute_integers(a1, a2):
    for i in range(a2):
        v4 = deterministic_number(i) % a2
        v3 = struct.unpack_from('I', a1, 4 * i)[0]
        struct.pack_into('I', a1, 4 * i, struct.unpack_from('I', a1, 4 * v4)[0])
        struct.pack_into('I', a1, 4 * v4, v3)
    return a2

def mix_integers(a1, a2, a3, a4):
    for i in range(a4):
        val = struct.unpack_from('I', a1, 4 * i)[0] + struct.unpack_from('I', a2, 4 * i)[0]
        struct.pack_into('I', a3, 4 * i, val)
    return a4

def derive_key_part1(a1):
    src = bytearray(64)
    hash_function(a1, 16, src)
    transform_integers(src, 16)
    return src

def derive_key_part2(a1):
    src = bytearray(64)
    hash_function(a1, 16, src)
    permute_integers(src, 16)
    return src

def derive_key_part3(a1):
    v3 = bytearray(64)
    hash_function(a1, 16, v3)
    mix_integers(a1, v3, a1, 16)
    return a1

def combine_key_parts(a1, a2, a3):
    src = bytearray(64)
    v8 = bytearray(64)
    xor_arrays(a1, a2, v8, 16)
    xor_arrays(v8, a3, src, 16)
    return src

def finalize_key(a1, a2):
    transform_integers(a1, a2)
    return permute_integers(a1, a2)

def generate_encryption_key(a1, a2):
    v3 = bytearray(64)
    v4 = bytearray(64)
    v5 = bytearray(64)
    v6 = bytearray(64)

    generate_deterministic_integers(v6, 16, a2)
    v5 = derive_key_part1(v6)
    v4 = derive_key_part2(v6)
    v3 = derive_key_part3(v6)
    a1 = combine_key_parts(v5, v4, v3)
    finalize_key(a1, 16)
    return a1

def key_expansion(a1, a2):
    for i in range(1337):
        for j in range(16):
            struct.pack_into('I', a2, (i << 6) + 4 * j, 7 * i + struct.unpack_from('I', a1, 4 * j)[0])

def transform_bytes(a1, a2, a3, a4):
    for i in range(a2):
        val = ((8 * a1[i]) | (a1[i] >> 5)) + a3[i % a4]
        a1[i] = val & 0xFF
    return a2

def permute_bytes(a1, a2):
    dest = bytearray(a2)
    for i in range(a2):
        dest[i] = a1[(7 * i) % a2]
    return dest

def obscure_function(a1, a2):
    for i in range(a2):
        a1[i] = ~a1[i] & 0xFF
    return a2

def xor_with_key(a1, a2, a3):
    for i in range(a2):
        a1[i] ^= a3[4 * (i & 0xF)]
    return a2

def custom_encrypt(a1, a2, a3):
    v6 = bytearray(1337 * 64)
    key_expansion(a3, v6)
    a4 = bytearray(a1)
    for i in range(1337):
        transform_bytes(a4, a2, v6[64 * i:64 * (i + 1)], 16)
        a4 = permute_bytes(a4, a2)
        xor_with_key(a4, a2, v6[64 * i:64 * (i + 1)])
        obscure_function(a4, a2)
    return a4

def reverse_obscure_function(a1, a2):
    # obscure_function was a bitwise NOT operation, so reversing it is the same
    return obscure_function(a1, a2)

def reverse_xor_with_key(a1, a2, a3):
    return xor_with_key(a1, a2, a3)  # XOR is its own inverse

def reverse_permute_bytes(a1, a2):
    dest = bytearray(a2)
    for i in range(a2):
        index = 7 * i % a2
        while index < 0:
            index += a2
        dest[index] = a1[i]
    return dest

def reverse_transform_bytes(a1, a2, a3, a4):
    for i in range(a2):
        original_val = a1[i]
        for _ in range(256):  # Brute-force to find the original byte value
            temp_val = ((8 * original_val | (original_val >> 5)) + a3[i % a4]) & 0xFF
            if temp_val == a1[i]:
                a1[i] = original_val & 0xFF
                break
            original_val -= 1
            if original_val < 0:
                original_val += 256  # Ensure it stays within valid byte range
    return a2

def custom_decrypt(a1, a2, a3):
    v6 = bytearray(1337 * 64)
    key_expansion(a3, v6)
    a4 = bytearray(a1)
    for i in range(1336, -1, -1):
        reverse_obscure_function(a4, a2)
        reverse_xor_with_key(a4, a2, v6[64 * i:64 * (i + 1)])
        a4 = reverse_permute_bytes(a4, a2)
        reverse_transform_bytes(a4, a2, v6[64 * i:64 * (i + 1)], 16)
    return a4

def main():
    s = bytearray(b"LEST2024{fake_flag_hehe}")
    v6 = bytearray(64)
    v6 = generate_encryption_key(v6, 1337)
    s_len = len(s)
    s = custom_encrypt(s, s_len, v6)
    print("Ciphertext:", ' '.join(str(b) for b in s))
    print("huh? what are you doing?")
    
    ciphertext = [243, 36, 117, 88, 109, 57, 143, 180, 178, 75, 121, 55, 98, 213, 216, 226, 114, 166, 206, 206, 75, 202, 107, 40, 197, 11, 219, 169, 165, 41, 69, 137, 143, 244, 245, 15, 21, 192, 66, 170]
    s = bytearray(ciphertext)
    v6 = bytearray(64)
    v6 = generate_encryption_key(v6, 1337)
    s_len = len(s)
    s = custom_decrypt(s, s_len, v6)
    print("Plaintext:", s.decode())

if __name__ == "__main__":
    main()
