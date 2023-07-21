import os
from colorama import Fore , init
import qrcode
import signal
import sys



def clear_terminal():
    # Check if the operating system is Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

# Call the function to clear the terminal
clear_terminal()

def signal_handler(signal, frame):
    print("")
    print(" Bye...")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Your code here


print(Fore.GREEN + ''' __   __      __   ___       ___  __       ___  __   __  
/  \ |__)    / _` |__  |\ | |__  |__)  /\   |  /  \ |__) 
\__X |  \    \__> |___ | \| |___ |  \ /~~\  |  \__/ |  \ 
                                                         ''')
print("  -----------------------------------------------------")
print("                                         Author: Z!L0X")
print("\n\n\n\n")





# Take input URL from the user
url=input(Fore.GREEN + " [?] Enter Url Here: ")

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code
print("")


img = qr.make_image(fill_color="black", back_color="white")
# Specify the filename for the QR code image
filename = input(Fore.GREEN + " [?] Enter File Name: ")
# Save the image to a file
img.save(filename + ".png")


print("")
print(" [√] Thank You For Using")




