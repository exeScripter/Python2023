# Importing modules
import requests
import json
import time
import os

# Clearing console
os.system('cls')

# Print welcome message
print('Welcome to Golden Boot Top 10')
print('This application is made by naroors#0001')
print('')
print('Choose year: ')
print("From 2014 to 2023")
print('')
input_year = input('Year: ')

# Clearing console
os.system('cls')

# Print the data from the year
print('Golden Boot Top 10 in ' + input_year)
print('')

# Get the data from folder 'data'
with open('data_container/' + input_year + '.txt') as f:
    # TXT
    data = f.read()
    print(data)

# Prevent the console from closing
input('Press enter to exit')




