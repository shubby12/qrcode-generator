from turtle import fillcolor
import qrcode


# Method 1

img = qrcode.make("https://shubhmyadav.netlify.app/")
img.save("Shubham's_Portfolio.png")




# Method 2

# from PIL import Image

# qr = qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_H, box_size=10, border=4)
# qr.add_data("https://shubhmyadav.netlify.app/")
# qr.make(fit=True)
# img=qr.make_image(fill_color="red", back_color="green")
# img.save("portfolio2.png")