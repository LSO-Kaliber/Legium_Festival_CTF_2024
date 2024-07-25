from PIL import Image

def decode_message(image_path):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    width, height = image.size
    message_bits = ""
    for y in range(height):
        for x in range(width):
            r, g, b = image.getpixel((x, y))
            message_bits += format(r, "08b")[-1]
            message_bits += format(g, "08b")[-1]
            message_bits += format(b, "08b")[-1]
    
    message_bytes = [message_bits[i:i+8] for i in range(0, len(message_bits), 8)]
    message = ''.join([chr(int(byte, 2)) for byte in message_bytes])
    return message.split("EOF")[0]

decoded_message = decode_message("secret.png")
print(decoded_message)