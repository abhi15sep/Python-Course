#Given a list ["Elie", "Tim", "Matt"], create a variable called answer, which is a new list containing the first letter of each name in the list.  I would use a list comprehension, though you could also loop over manually.
#Given a list [1,2,3,4,5,6], create a new variable called answer2, which is a new list of all the even values.  Another good candidate for a list comp.

#Using list comprehensions:

answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]


#Using good old manual loops:

answer = []
for person in ["Elie", "Tim", "Matt"]:
    answer.append(person[0])
answer2 = []
for num in [1,2,3,4,5,6]:
    if num % 2 == 0:
        answer2.append(num)
