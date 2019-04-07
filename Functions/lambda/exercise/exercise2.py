#Write a function called decrement_list  that accepts a single list of numbers as a parameter.  It should return a copy of the list where each item has been decremented by one. Use map to do this! For example:
#decrement_list([1,2,3]) #[0,1,2]
#decrement_list([20,14,11]) #[19,13,10]


#decrement_list solution

def decrement_list(l):
    return list(map(lambda n: n-1, l))
