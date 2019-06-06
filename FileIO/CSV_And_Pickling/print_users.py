#For this exercise, you'll be working with a file called "users.csv" . Each row of data consists of two columns: a user's first name, and a user's last name.
#Implement the following function:
#"print_users"  : prints out all of the first and last names in the "users.csv" file.


'''
print_users() # None
# prints to the console:
# Abhay Singh
'''

import csv


def print_users():
    with open("users.csv") as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            print("{} {}".format(row['First Name'], row['Last Name']))
