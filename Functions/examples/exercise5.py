#The pre-written count_dollar_signs function is broken. It's supposed to return the number of "$"  characters in a given string.  For example:
#count_dollar_signs("$uper $ize")  should return 2.  .  But for some reason, the function always returns either 0 or 1. What's going on?
#Without adding any new lines (just move existing code around), make it work as intended.

# Without adding any new lines of code, make count_dollar_signs work as intended


#Here's the initial broken state of the function:

def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
        return count
#The problem is that the function returns the very first time through the loop because of the way return is indented.

#To fix it, all we have to do is outdent the return statement so that it now only returns after the loop finishes running

def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count
