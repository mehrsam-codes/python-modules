import qrcode

data = "https://github.com/mehrsam-codes"

qr = qrcode.make(data)
qr.save("github_qr.png")

print("QR Code ساخته شد.") #translate to english = qr code created 