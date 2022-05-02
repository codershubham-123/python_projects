# importing the qrcode library
import qrcode as qr
# generating the qr code using make function
img = qr.make("https://www.google.com/")
# save the image
img.save("QR-img.jpg")