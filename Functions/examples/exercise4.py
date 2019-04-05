#Implement a function yell which accepts a single string argument.  It should return(not print) an uppercased version of the string with an exclamation point aded at the end.  For example:
# yell("go away")   # "GO AWAY!"
#yell("leave me alone")     # "LEAVE ME ALONE!"
#You do not need to call the function to pass the tests.


#Using string concatenation:
def yell(word):
    return word.upper() + "!"

#Using the string format() method:
def yell(word):
    return "{}!".format(word.upper())

#Using an f-string. But only works in python 3.6 or later.
def yell(word):
    return f"{word.upper()}!"
