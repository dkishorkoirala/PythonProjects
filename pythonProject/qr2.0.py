import os 
import qrcode

#asking for input
link = input("Enter the Link: ")

#generate and save the qr image
img = qrcode.make(link)
img.save("qr.png","PNG")

#open the generated qr code image using the appropriate command for the platform 
if os.name == "posix": #macos or linux
    os.system("open qr.png")
elif os.name == "nt": #windows
    os.system("start qr.png")
else:
    print("Unsupported operating system.")


print("QR code generated and opened successfully.")
