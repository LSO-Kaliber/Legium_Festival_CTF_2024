def logo():
    print "\nScramble Python\n"

def main():
    inputUser = raw_input("Ayo cek flagnya mas: ")
    splitString = list(inputUser)
    flage = []
    for i in range(0, len(splitString)):
        flag = ord(splitString[i]) + 0xd3c0d3 + 0x51203
        flage.append(flag)
    if len(flage) == 53:
        if (flage[41] == 14209845 and
            flage[14] == 14209862 and
            flage[4] == 14209800 and
            flage[38] == 14209799 and
            flage[0] == 14209826 and
            flage[26] == 14209860 and
            flage[25] == 14209798 and
            flage[17] == 14209855 and
            flage[32] == 14209801 and
            flage[27] == 14209845 and
            flage[51] == 14209851 and
            flage[40] == 14209851 and
            flage[48] == 14209804 and
            flage[20] == 14209845 and
            flage[16] == 14209858 and
            flage[29] == 14209802 and
            flage[35] == 14209871 and
            flage[11] == 14209849 and
            flage[45] == 14209847 and
            flage[3] == 14209834 and
            flage[15] == 14209799 and
            flage[13] == 14209859 and
            flage[44] == 14209849 and
            flage[12] == 14209861 and
            flage[19] == 14209853 and
            flage[47] == 14209852 and
            flage[39] == 14209859 and
            flage[1] == 14209819 and
            flage[52] == 14209875 and
            flage[43] == 14209848 and
            flage[36] == 14209845 and
            flage[46] == 14209852 and
            flage[23] == 14209866 and
            flage[42] == 14209806 and
            flage[9] == 14209850 and
            flage[10] == 14209801 and
            flage[28] == 14209869 and
            flage[31] == 14209866 and
            flage[49] == 14209847 and
            flage[24] == 14209854 and
            flage[21] == 14209862 and
            flage[22] == 14209871 and
            flage[7] == 14209802 and
            flage[33] == 14209845 and
            flage[18] == 14209860 and
            flage[50] == 14209800 and
            flage[5] == 14209798 and
            flage[6] == 14209800 and
            flage[37] == 14209866 and
            flage[8] == 14209873 and
            flage[30] == 14209865 and
            flage[34] == 14209859 and
            flage[2] == 14209833):
                print "Benar mas, itu flagnya."
        else:
            print "Itu bukan flagnya mas."
    else:
        print "Itu bukan flagnya mas."
        
if __name__ == "__main__":
    logo()
    main()