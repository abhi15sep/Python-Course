#You will be provided with a random number in a variable called num.
#Use a conditional statement to check if the number is odd. If num is odd, print "odd". Otherwise print "even".
#Himt: use modulus % to figure out if number is odd.


# NO TOUCHING ======================================
from random import randint

num = randint(1, 1000)
# NO TOUCHING ======================================


# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
if num % 2 != 0:
    print("odd")
else:
    print("even")