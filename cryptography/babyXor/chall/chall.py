import random

flag = 'LEST2024{xor_chall3nGe_maK3_Me_h4pPy}'  # This is dummy flag
key_1 = [random.randint(1, 200) for _ in range(2)]
key_2 = [random.randint(1, 500) for _ in range(2)]


def enc(src, key):
    res = []
    for a, b in enumerate(src):
        if (a % 2 == 0):
            res.append(ord(b) ^ key[0])
        else:
            res.append(ord(b) ^ key[1])
    return res


res_1 = enc(flag, key_1)
res_2 = enc(flag, key_2)
print(res_2)

# output : [359, 216, 376, 201, 281, 173, 281, 169, 336, 229, 324, 239, 372, 254, 323, 252, 327, 241, 280, 243, 364, 248, 372, 240, 330, 214, 280, 194, 358, 248, 372, 245, 287, 237, 379, 228, 342]
