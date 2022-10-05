
import os
import sys
import time
import requests

# Ascii text from a file
with open("sigmarules.txt") as f:
    text = f.read()

# Update Checker - Checks for updates from github link
def update():
    try:
        r = requests.get("https://raw.githubusercontent.com/0x00-0x00/Python-Projects/master/sigmarules.py")
        if r.status_code == 200:
            with open("sigmarules.py", "w") as f:
                f.write(r.text)
            print("Updated!")
            time.sleep(2)
            os.system("cls")
            os.system("sigmarules.py")
        else:
            print("No updates available!")
    except:
        print("No internet connection!")
        


# Clear the screen
os.system("cls")

# Print the text
for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.01)


# Run the rest of the program
print("")
print("Welcome, here you can find the best rules/quotes.")
print("Choose one of the options below:")

print("1. Rules")
print("2. Quotes")
print("3. Changelog")
print("4. Update")
print("5. Exit")

# Get the user's choice
choice = input("Your choice: ")



if choice == "1":
    # Clear the screen
    os.system("cls")

    # Print the text
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    
    print ("")

    # Print the rules
    print("1. Don't apologize for being yourself.")
    print("2. Work on your weaknesses.")
    print("3. Don't be afraid to fail.")
    print("4. First money, then love")
    print("6. Change your environment.")
    print("7. Push yourself.")
    
    # Prevent the program from closing
    input("Press enter to exit")



elif choice == "2":
    # Clear the screen and print the ascii again
    os.system("cls")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    # Print the quotes
    print("1. “Everyone has a Lambo or a Ferrari, it’s easy.” - Andrew Tate")
    print("2. “Do you not see how the elites play you?“ - Andrew Tate")
    print("3. “You must work on yourself and stop looking at what society wants you to be” - Andrew Tate")
    print("4. ”When somebody challenges you, fight back. Be brutal, be tough.” - Donald Trump")

    # Press enter to exit
    input("Press enter to exit")


elif choice == "3":
    # Clear the screen and print the ascii again
    os.system("cls")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    # Print the changelog
    print("1. Added quotes")
    print("2. Added rules")
    print("3. Added changelog")
    print("4. Added exit option")

    # Press enter to exit
    input("Press enter to exit")

elif choice == "4":
    # Clear the screen and print the ascii again
    os.system("cls")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    # Run the update checker
    update()


elif choice == "5":
    # Clear the screen and print the ascii again
    os.system("cls")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    # Print the exit message
    print("Thank you for using this program, goodbye!")

    # Press enter to exit
    input("Press enter to exit")






# Make the program not close
input("Press enter to exit")

