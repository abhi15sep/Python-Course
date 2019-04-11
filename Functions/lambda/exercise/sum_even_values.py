#Write a function called "sum_even_values". This function should accept a variable number of arguments and return the sum of all the arguments that are divisible by 2. If there are no numbers divisible by 2, the function should return 0.  To be clear, it accepts all the numbers as individual arguments!


def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0)
