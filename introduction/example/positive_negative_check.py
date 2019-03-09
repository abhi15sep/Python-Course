# In this exercise x and y   are two random variables.  The code at the top of the file randomly assigns them.
#1) If both are positive numbers, print "both positive".
#2) If both are negative, print "both negative".
#3) Otherwise, tell us which one is positive and which one is negative, e.g. "x is positive and y is negative"

# NO TOUCHING ======================================
from random import randint

x = randint(-100, 100)
while x == 0:  # make sure x isn't zero
    x = randint(-100, 100)
y = randint(-100, 100)
while y == 0:  # make sure y isn't zero
    y = randint(-100, 100)
# NO TOUCHING ======================================

# YOUR CODE GOES HERE

if x > 0 and y > 0:
    print("both positive")
elif x < 0 and y < 0:
    print("both negative")
elif x > 0 and y < 0:
    print("x is positive and y is negative")
else:
    print("y is positive and x is negative")
    print("y is positive and x is negative")
    print("y is positive and x is negative")