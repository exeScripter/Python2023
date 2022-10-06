# Make a dowmload of a py file from the github link

import requests
import os
import sys

with open("hu3.txt", "w") as f:
    f.read()


# Download the file and print the status code
r = requests.get("https://raw.githubusercontent.com/0x00-0x00/Python-Projects/master/sigmarules.py")
print(r.status_code)

# Write the file
with open("sigmarules.py", "w") as f:
    f.write(r.text)

# Run the file
os.system("sigmarules.py")

# Close the program
sys.exit()
