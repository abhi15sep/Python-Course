#Define a function called "contains_keyword" that accepts  any number of string arguments.  It should return True  if any of the arguments are considered Python keywords (things like "def", "return", "if", etc.)  Otherwise it should return False.
#   Python has a built-in module called "keyword"  that contains a method called iskeyword .  Import keyword  and then use keyword.iskeyword  in you own function to determine if a given string is a keyword.

#contains_keyword("hello", "goodbye")   #False
#contains_keyword("def", "haha", "lol", "chicken", "alaska")   #True
#contains_keyword("four", "for", "if")   #True
#contains_keyword("blah", "doggo", "crab", "anchor")   #False

import keyword


def contains_keyword(*args):
    for item in args:
        if keyword.iskeyword(item): return True
    return False
