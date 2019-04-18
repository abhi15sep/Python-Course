#This exercise has two files!!!
#Your task is to write a function in the helpers.py file, and then call it from the exericse.py file.  More specifically:
# 1.In helpers.py, define a function called lucky_number()  that always returns the number 37.  That's it.   It always returns 37, no matter what.
# 2. In exercise.py, import the helpers module.  In order for the testing logic to work properly, don't use the 'as', or 'from' keywords when importing.  Just do a plain old import.
# 3. From inside exercise.py, call the lucky_number  function you defined in the helpers module. Save the result to a variable called num

#In helpers.py:
def lucky_number():
    return 37

#In exercise.py:
# Import your helpers module here.  Do not use the 'from' or 'as' syntax, just use a plain old 'import'
import helpers

# Call the lucky_number function from your helpers module, and save the result to a variable called num
num = helpers.lucky_number()
