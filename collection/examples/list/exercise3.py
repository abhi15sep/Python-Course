#List Iteration Exercise
#I've given you a list called sounds.
#sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
#1 Write code that loops over the list and adds all the strings together to form one large combined string (don't add any spaces between them)
#2 The combined string should be in all UPPERCASE as well
#3 Save the result in a variable called result

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s.upper()



sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s
result = result.upper()
