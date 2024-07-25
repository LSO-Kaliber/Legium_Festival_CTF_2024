string = "LEST2024{d3comp1ling_pyth0n_w4st3_my_t1me_8bcaff6a2e}"

for i in range(len(string)):
    encoded_value = ord(string[i]) + 0xd3c0d3 + 0x51203
    print(f"flage[{i}] == {encoded_value} and")