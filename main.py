import qrcode

features = qrcode.QRCode(version=1, box_size=40, border=5)
features.add_data('https://www.youtube.com/watch?v=tSiS15ubQFQ&list=PLo4zRL1NfXkfVjEO6eo5N_kzw0P8Ww3ml')
features.make(fit=True)
generate_image = features.make_image(fill_color="black", back_color="white")
generate_image.save("image6.png")