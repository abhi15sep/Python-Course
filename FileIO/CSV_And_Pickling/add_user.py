#For this exercise, you'll be working with a file called "users.csv" . Each row of data consists of two columns: a user's first name, and a user's last name.
#Implement the following function:
#"add_user"  : Takes in a first name and a last name and adds a new user to the "users.csv" file.


'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Abhay,Singh
# Dwayne,Johnson
'''

import csv


def add_user(first_name, last_name):
    with open("users.csv", "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([first_name, last_name])
