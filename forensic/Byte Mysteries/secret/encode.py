from PIL import Image

def encode_message(image_path, message):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    if image.mode != 'RGB':
        image = image.convert('RGB')

    encoded = image.copy()
    width, height = image.size
    message += "EOF"
    message_bits = ''.join([format(ord(i), "08b") for i in message])
    message_length = len(message_bits)
    
    index = 0
    for y in range(height):
        for x in range(width):
            if index < message_length:
                r, g, b = image.getpixel((x, y))
                r = int(format(r, "08b")[:-1] + message_bits[index], 2)
                index += 1
                if index < message_length:
                    g = int(format(g, "08b")[:-1] + message_bits[index], 2)
                    index += 1
                if index < message_length:
                    b = int(format(b, "08b")[:-1] + message_bits[index], 2)
                    index += 1
                encoded.putpixel((x, y), (r, g, b))
    encoded.save("flag.png")

encode_message("secret.png", "LEST2024{NuC134R_5ECRE7T_unv3!LEd_2024}")
