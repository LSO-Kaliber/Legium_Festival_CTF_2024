from random import randint
from secret import message

flag = message
l = 26

def plugs():
    start = 96
    plugs_len = randint(1, 6)
    result = []
    used_numbers = set()
    while len(result) < plugs_len:
        x, y = randint(1, l), randint(1, l)
        if x not in used_numbers and y not in used_numbers and x != y:
            used_numbers.add(x)
            used_numbers.add(y)
            result.append([chr(x + start), chr(y + start)])
    return result

def rotos():
    result = []
    rotos_len = randint(3, 6)
    while len(result) < rotos_len:
        rotos_set = randint(1, l)
        result.append(rotos_set)
    return result

def rotos_rotate(rot):
    return rot + 1

def write(data):
    with open("output.txt", "w") as file:
        file.write(str(data))

def enc(settings, message):
    s, e = (97, 123)
    plug_settings, rotor_settings = settings
    chr_controller = []
    encMessage = ""
    for char in message:
        
        rotor_settings[-1] = rotos_rotate(rotor_settings[-1])
        for i in range(len(rotor_settings) - 1, -1, -1):
            if rotor_settings[i] > l:
                rotor_settings[i] = 1
                if i != 0:
                    rotor_settings[i - 1] += 1
            else:
                break
        rot_len = sum(rotor_settings)
        char = ord(char) + rot_len

        loop_ex = 0
        while(char >= e):
            loop_ex += 1
            char -= (e - s)
        chr_controller.append(loop_ex)
        char = chr(char)

        for plug in plug_settings:
            if char == plug[0]:
                char = plug[1]
            elif char == plug[1]:
                char = plug[0]

        encMessage += char

    return [encMessage, chr_controller]

def today_setting():
    plug_settings = plugs()
    rotor_settings = rotos()
    settings = [plug_settings, rotor_settings]
    encrypted_message = enc(settings, flag)

    print(settings) #The setting is described in the letter.
    write(('message', encrypted_message))

today_setting()

#################################################################################################################################
##                                                                                                                             ##
##  Einstellung - JULY 1944                                                                                                    ##
##                                                                                                                             ##
##  From : Berlin                                                                                                              ##
##  To   : München                                                                                                             ##
##                                                                                                                             ##
##                                                                                                                             ##
##  Heil, mein Führer!                                                                                                         ##
##                                                                                                                             ##
#################################################################################################################################
##           ##                                                                                                                ##
##   Day 1   ##       [[['v', 'o'], ['z', 'b'], ['j', 't'], ['y', 'n'], ['w', 'h'], ['a', 's']], [4, 3, 18, 7, 15, 24]]        ##
##           ##                                                                                                                ##
#################################################################################################################################