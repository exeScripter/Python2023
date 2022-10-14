# Check if user has acces to the program, if not, exit

# Import modules
import os
import sys
import time
import wget
import pyfiglet

# ASCII art
w = pyfiglet.figlet_format("REGISTER | FORM")
print(w)

# Print the register
print("Welcome to the register form!")
print("Please enter your username and password to continue.")
print("-----------------------------")
print("NOTE: If you already have an account, please login.")
print("-----------------------------")
print("")

# Ask for the user's data
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if the username or email is already in the database, if yes inform the user
userdata = open("database.txt", "r")
if username in userdata.read():
    # Check if password is weak, password must contain at least 8 characters, 1 uppercase letter, 1 lowercase letter, 1 number.
    if len(password) < 8:
        print("Your password is too weak!")
        print("Please try again.")
        print("-----------------------------")
        print("")

        time.sleep(2)
        sys.exit()
    
    else:
        print("Checking your data...")
        time.sleep(2)

        print("-----------------------------")
        print("Username already in use!")
        print("-----------------------------")
        print("")
        print("Please log in")
        time.sleep(2)
        sys.exit()
else: 
    # Check if password is weak
    if len(password) < 8:
        print("Your password is too weak!")
        print("Please try again.")
        print("-----------------------------")
        print("")

        time.sleep(2)
        sys.exit()
    
    else:
        print("Checking your data...")
        time.sleep(2)


        # If the username or email is not in the database, add it to the database
        userdata = open("database.txt", "a")
        # Add a new line to the database
        userdata.write("\n")
        userdata.write(username + ":" + password)
        userdata.close()

        # Print the success message
        print("-----------------------------")
        print("Account created successfully!")
        print("-----------------------------")
        print("Please log in")

        time.sleep(2)
        sys.exit()

    
