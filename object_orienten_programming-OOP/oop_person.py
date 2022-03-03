
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1
        pass

print(Person.number_of_people)

p1 = Person("aaa")

print(Person.number_of_people)

p2 = Person("bbb")

print(Person.number_of_people)

Person.number_of_people = 8 #changing definition of variable in class

print(p1.number_of_people)