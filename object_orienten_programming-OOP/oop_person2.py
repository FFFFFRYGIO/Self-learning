
class Person:
    number_of_people = 0

    def __init__(self, name): #self to take obcject variable / attribute
        self.name = name
        Person.add_person()
        pass

    @classmethod
    def get_number_of_people(cls): #cls to take class variable
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("aaa")
p2 = Person("bbb")

print(Person.get_number_of_people())