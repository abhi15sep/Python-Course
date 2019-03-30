#Given a person variable:
#person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
#Create a dictionary called answer , that makes each first item in each list a key and the second item a corresponding value.  That's a terrible explanation.  I think it'll be easier if you just look at the end goal:
# {'name': 'Jared', 'job': 'Musician', 'city': 'Bern'}

#Using a dictionary comprehension
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}

#using a dict comprehension, without any references to list indexes:
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {k:v for k,v in person}

#If you have a list of pairs, you can very easily turn it into a dictionary using dict()
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = dict(person)
