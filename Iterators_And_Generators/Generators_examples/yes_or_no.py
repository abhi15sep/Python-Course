#Write a function called "yes_or_no", which returns a generator that first yields "yes" , then "no" , then "yes" , then "no" , and so on.

'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''

#yes_or_no  loops forever (while True) and yields answer , and then toggles answer from yes to no, or vice versa.

def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"


gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'