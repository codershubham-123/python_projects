# importing the qrcode library
import qrcode as qr
# Creating the qr code object
qr_obj = qr.QRCode(
    version= 1,
    error_correction= qr.constants.ERROR_CORRECT_H,
    box_size= 10,
    border= 4
)
# Using add_data function
qr_obj.add_data("https://www.hackerrank.com/access-account/")
# using the make function
qr_obj.make(fit=True)
# using the make_image function
qr_img = qr_obj.make_image(fill_color = "red", back_color = "white")
# save the image
qr_img.save("Ad_QR.jpg")

