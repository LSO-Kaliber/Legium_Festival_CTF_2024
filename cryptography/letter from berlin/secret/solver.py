def dec(settings, message):
    hint = message[1]
    msg = message[0]
    dec_message = ''
    rotor_settings_history = []
    settings[1][len(settings[1]) - 1] = settings[1][len(settings[1]) - 1] + 1

    def decrement_rotors(rotors):
        paanjang = len(rotors) - 1
        rotors[paanjang] -= 1
        while paanjang > 0 and rotors[paanjang] == 0:
            rotors[paanjang] = 26
            paanjang -= 1
            rotors[paanjang] -= 1

    for _ in msg:
        decrement_rotors(settings[1])
        rotor_settings_history.append(settings[1][:]) 

    rotos_len = len(rotor_settings_history) - 1
    for i, char in enumerate(msg):
        for plug in settings[0]:
            if char == plug[0]:
                char = plug[1]
            elif char == plug[1]:
                char = plug[0]
        rotos = sum(rotor_settings_history[rotos_len])

        plus = hint[i] * 26
        char = chr((ord(char) + plus) - (rotos))
        dec_message += char
        rotos_len -= 1
    print(dec_message)

settings = [[['v', 'o'], ['z', 'b'], ['j', 't'], ['y', 'n'], ['w', 'h'], ['a', 's']], [4, 3, 18, 7, 15, 24]]
message = ['enypiwkywmhctbqzyhehbsdowjmsozhtaqjwihusoiufbo', [1, 0, 1, 1, 0, 0, 0, 0, 3, 0, 1, 3, 2, 2, 0, 2, 2, 0, 3, 0, 2, 2, 0, 1, 2, 2, 1, 3, 2, 2, 2, 0, 2, 1, 2, 1, 2, 1, 1, 2, 0, 3, 0, 3, 1, 3]]
dec(settings, message)