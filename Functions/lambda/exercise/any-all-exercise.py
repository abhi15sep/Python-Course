#Implement a function "is_all_strings"   that accepts a single iterable and returns True if it contains ONLY strings.  Otherwise, it should return false.
#is_all_strings(['a', 'b', 'c'])   #True
#is_all_strings([2,'a', 'b', 'c'])   #False
#is_all_strings(('hello', 'goodbye'))   #True


#Using a Generator Expression

def is_all_strings(lst):
    return all(type(l) == str for l in lst)

#Using a List Comprehension

def is_all_strings(lst):
    return all([type(l) == str for l in lst])
