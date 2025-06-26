import qrcode

def generate_qr():
    while True:
        data = input("Enter the text or URL to generate QR code (or type 'exit' to quit): ")
        if data.lower() == 'exit':
            break
        filename = input("Enter filename to save (without extensions): ")
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(f"{filename}.png")
        print(f"QR code saved as {filename}.png")

generate_qr()