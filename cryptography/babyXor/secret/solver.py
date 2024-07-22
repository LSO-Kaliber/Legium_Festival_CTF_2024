cipher_txt = [359, 216, 376, 201, 281, 173, 281, 169, 336, 229, 324, 239, 372, 254, 323, 252, 327, 241, 280, 243, 364, 248, 372, 240, 330, 214, 280, 194, 358, 248, 372, 245, 287, 237, 379, 228, 342]

def key_1():
    for key_2 in range(0, 501):
        for key_1 in range(0, 201):
            res = ""
            for a, b in enumerate(cipher_txt):
                if(a % 2 == 0):
                    res += chr(b ^ key_2 ^ key_1)
            if(res[0] == "L" and res[1] == 'S'):
                return key_2 ^ key_1

def key_2():
    for key_2 in range(0, 501):
        for key_1 in range(0, 201):
            res = ""
            for a, b in enumerate(cipher_txt):
                if(a % 2 == 1):
                    res += chr(b ^ key_2 ^ key_1)

            if(res[0] == "E" and res[1] == 'T'):
                return key_2 ^ key_1

key_1 = key_1()
key_2 = key_2()

res = ""
for a, b in enumerate(cipher_txt):
    if(a % 2 == 0):
        res += (chr(b ^ key_1))
    if(a % 2 == 1):
        res += (chr(b ^ key_2))

print(res)