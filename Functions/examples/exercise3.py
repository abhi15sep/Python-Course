#Write a function called generate_evens  that returns a list of the even numbers between 1 and 50(not including 50).
#Basically, it should return a list: [2,4,6....all the way up to 48]
# Inside the function, you can construct the list using either a loop OR list comprehension.
#You do not need to call the function in this exercise, defining it is enough.

#Generating evens using a list comprehension:

def generate_evens():
    return [x for x in range(1,50) if x%2 == 0]

#Generating evens using a loop:

def generate_evens():
    result = []
    for x in range(1,50):
        if x % 2 == 0:
            result.append(x)
    return result
