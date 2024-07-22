from Crypto.Util.number import getStrongPrime, bytes_to_long
from egcd import egcd
from secret import flag, nbit
from time import sleep

primeNumber = getStrongPrime(nbit)
result_i = []

def encrypt_flag(flag):
    N = primeNumber
    result_i.clear()
    for i in range(nbit):
        if egcd(flag, i)[0] == 1:
            N *= i
            result_i.append(i)
        
    cp = pow(flag, 65537, N)
    return cp
    
def check_flag():
    user_inp = str(input("input known flag: ")).strip()
    user_flag = encrypt_flag(bytes_to_long(user_inp.encode()))
    enc_flag = encrypt_flag(flag)
    if enc_flag == user_flag:
        print("Yep it's true")
    else:
        print("Nope..")

def menu():
    print("\n=== WHAT IS THIS??? MENU ===")
    print("what do you want?")
    print("1. flag")
    print("2. check flag")
    print("3. exit")
    
if __name__ == "__main__":
    while True:
        try:
            menu()
            choose = int(input("input>> "))
            print("wait for a moment....\n")
            sleep(1)
            if choose == 1:
                print(f"Here your flag: {encrypt_flag(flag)}")
            elif choose == 2:
                check_flag()
            elif choose == 3:
                break
        except Exception as e:
            print(e)
            print("Some error happen!")