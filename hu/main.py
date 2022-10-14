# Check if user has acces to the program, if not, exit

# Import modules
import os
import sys
import time
import wget
import pyfiglet


# ASCII art
w = pyfiglet.figlet_format("LOGIN | SYSTEM")
print(w)

# Print the login system
print("Welcome to the login system!")
print("Please enter your username and password to continue.")
print("-----------------------------")
print("NOTE: If you don't have an account, please create one.")
print("-----------------------------")
print("")

# Ask for the user's data
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the user has access to the program from the database
userdata = open("database.txt", "r")
if username and password in userdata.read():
    print("[+] Checking your data...")

    time.sleep(2)


    # Print Success
    print("-----------------------------")
    print("[+] Access granted!")
    time.sleep(2)
    print("-----------------------------")
    input("Press ENTER to continue...")
    print("-----------------------------")

    # Print 50 blank lines
    print('\n' * 50)

    # Print the menu in ASCII
    menu_banner = pyfiglet.figlet_format("Main Program")
    print(menu_banner)

    # Print the menu
    print("Welcome to the main program!")
    print("Please select an option from the menu below.")
    print("-----------------------------")
    print("1. Join Discord")
    print("2. Open the Website")
    print("3. Download the Client")
    print("4. Logout")
    print("-----------------------------")
    print("")
    option = input("Enter your option: ")

    # Check if the user has selected a valid option
    if option == "1":
        print("Opening Discord...")
        time.sleep(2)
        os.system("start https://discord.gg/4q3yU6N3")
        sys.exit()

    elif option == "2":
        print("Opening the website...")
        time.sleep(2)
        os.system("start https://realworld.ai/")
        # if the website is not available, print an error message
        print("The website is not available at the moment.")
        print("Please try again later.")
        time.sleep(2)
        sys.exit()

    elif option == "3":
        print("Downloading the client...")
        time.sleep(2)
        wget.download("https://realworld.ai/download")
        sys.exit()

    elif option == "4":
        print("Logging out...")
        time.sleep(2)
        sys.exit()
        
    
    else:
        print("Invalid option!")
        time.sleep(2)
        sys.exit()

else:
    print("[+] Checking your data...")
    time.sleep(2)

    print("-----------------------------")
    print("[-] Access denied!")
    print("-----------------------------")
    print("")
    print("Download the registration client?")
    print("1. Yes")
    print("2. No")
    print("-----------------------------")
    print("")
    option = input("Enter your option: ")

    if option == "1":
        print("Downloading the registration client...")
        time.sleep(2)
        wget.download("")
        sys.exit()

    time.sleep(2)
    sys.exit()
