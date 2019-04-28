class Human:
    def __init__(self, first, last, age=0):
        self.first = first
        self.last = last
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError('\'age\' attribute can\'t be negative')


jane = Human("Jane", "Perry", 34)
print(jane.age)
jane.age = 40
print(jane.age)
