import base64

for i in range(1, 37):
    # Membaca file gambar
    image_file_path = f"{i}.png"
    with open(image_file_path, "rb") as image_file:
        # Membaca konten gambar
        image_content = image_file.read()

        # Mengonversi gambar menjadi base64
        base64_encoded = base64.b64encode(image_content).decode('utf-8')

        # Menyimpan hasil ke file teks
        output_file_path = f"hasil-{i}.txt"
        with open(output_file_path, "w") as output_file:
            output_file.write(base64_encoded)

        print(f"File {image_file_path} berhasil diubah menjadi base64 dan disimpan di {output_file_path}")
