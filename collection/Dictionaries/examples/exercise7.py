#Given two lists ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"] create a dictionary that looks like this {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}. Save it to a variable called answer.
#I expect you to do this with a dictionary comprehension, but you can also use a built-in function called zip.

#Using a dictionary comprehension:
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
answer = {list1[i]: list2[i] for i in range(0, 3)}


#Advanced" solution using zip
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
dict(zip(list1, list2))
