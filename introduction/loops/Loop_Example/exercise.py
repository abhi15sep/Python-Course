# Use a for loop to add up every odd number  from  10 to 20 (inclusive) and store the result in the variable x.
# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0

# YOUR CODE GOES HERE:
#Solution Using a Conditional
for n in range(10, 21):  #remember range is exclusive, so we have to go up to 21
    if n % 2 != 0:
        x += n

#Solution using range step
#Instead of looping over every number between 10 and 20, this solution only loops over the odd numbers.  Remember, the 3rd argument to range() is the STEP or interval that you want the range to increment by.

x = 0

for i in range(11, 21, 2):
    x += i
