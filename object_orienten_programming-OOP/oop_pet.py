class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak():
        print("I dont speak")

class Cat(Pet): #inheritance

    def __init__(self, name, age, color):
        super().__init__(name, age) #fetching inits from base class
        self.color = color

    def speak(self): #polymorphism
        print("Meaw")

class Dog(Pet):
    
    def speak(self):
        print("Bark")

