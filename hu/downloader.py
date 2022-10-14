# Make an ASCII animated art using py figlet and download the file using wget

import os
import sys
import time
import wget
import pyfiglet

# ASCII art
ascii_banner = pyfiglet.figlet_format("OI Downloader")
print(ascii_banner)

# Downloading the file
url = "https://raw.githubusercontent.com/exeScripter/Python2023/main/sigmarules.txt"
wget.download(url, "sigmarules.txt")

# Display the process
print("")
print("-----------------------------")
print("Downloading the file...")
time.sleep(2)
print("-----------------------------")
print("File downloaded successfully!")
time.sleep(2)

# Exit
print("")
print("Exiting...")

# End of the program
os.system("pause")
