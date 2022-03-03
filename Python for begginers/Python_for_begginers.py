#python D:\Programowanie\Python_for_begginers.py

def lesson1(): #1: Introduction to Python programming
    print("Introduction to Python programming")
    # Zastosowanie:
    #     Machine Learning
    #     Web development
    # 	Data Analysis
    # 	Scientific Research
    # 	Automation
    print("Hello world")

def lesson2(): #2: Python print() function and variables
    print("Python print() function and variables")
    x=1
    print(x)
    print('x')
    print("x")

    city="kathmandu"
    print(city)
    print("city")
    print("City:", "Kathmandu") #wyświetli się ze spacją między stringami

def lesson3(): #3: How to Take User Input in Python?
    number = input("Input number: ")
    print(number)
    print(type(number))
    number = int(number)
    print(type(number))
    number2 = float(input("Input number: "))
    print(type(number2))

def lesson4(): #4: Comments in Python
    '''Tutaj jest
    wieloliniowy komentarz'''

def lesson5(): #5: Operators in Python
    import math
    x = 8
    print(type(x))
    result = x / 10
    print(result)
    print(type(x))
    print(type(result))
    print(x ** 2) # x to the power of 2
    print(x // 3) # root of 3rd degree of x 
    print(x % 2, x % 3, x % 4, x % 5)
    x += 5 #x = x + 5
    x -= 5 #x = x - 5
    
    print("float result of square root")
    x = float(x)
    result = math.sqrt(x)
    print(result)
    print(type(result))
    result = x // 2 #floor division
    print(result)
    print(type(result))
    result = x ** (1.0/2)
    print(result)
    print(type(result))
    result = math.pow(x, 1.0/2)
    print(result)
    print(type(result))
    
    str1, str2 = "ABC ", "abc" #space to seperate text from str1 and str2
    print(str1, str2, str1 + str2) #double space - from str1 and from print

def lesson6(): #6: Python Booleans and Comparison Operators
    b1 = True
    b2 = False
    number = 5
    print(number < 6)
    print(not number < 6)
    print('10' == 10)
    result = b1 or b2
    print('result = %r or %r\t\tresult = %r' % (b1, b2, result))
    result = b1 and b2
    print('result = %r and %r\t\tresult = %r' % (b1, b2, result))
    result = b1 ^ b2
    print('result = %r ^ %r (xor)\t\tresult = %r' % (b1, b2, result))

def lesson7(): #7: Python if...else Statement for Decision Making
    x = True
    if x:
        print("YES")
    elif x == False:
        print("CHUJ")
    else:
        print("GYYY")

def lesson8(): #8: Python while Loop to Repeat Code
    x = 5
    while x:
        print("UWU")
        x -= 1

def lesson9(): #9: for Loop in Python
    text = "Python"
    print(text)
    for i in text:
        print(i)
    text2 = ['P','y','t','h','o','n']
    print(text2)
    for i in text2:
        print(i)

    for number in range(10): #From 0 to 9, excluding 10
        sum = 0
        for i in range(0,number+1):
            sum += i
        print('sum from 0 to ',number,' is ',sum)

def lesson10(): #10: break & continue in Python
    for i in range(10): #is printing 00 11 22 33 44 5
        print(i)
        if(i == 5):
            break
        print(i)
    for i in range(10): #is printing 000 111 222 333 444 555 6 7 8 9
        print(i)
        if(i > 5):
            continue #go to next step in loop, ignore the following instructions
        print(i)
        print(i)

    letters = ['A','B','C','D','E','F']
    for i in letters:
        if i == 'C' or i == 'E':
            continue
        print(i)

def lesson11(): #11: pass Statement in Python
    if True:
        #You cannot end program this way, to fix it you can type "pass"
        pass

def lesson12(): #12: Python Functions (The Only Guide You'll Need)
    #3 types of functions:
        #create a circle
        #create a rectangle
        #color the shape
    text = 'Python'
    def length(x):
        return(len(x))
    print("Length of x is",length(text))

    numbers = [0,1,2,3,4,5,6,7,8,9,10]
    def summary(list1):
        return sum(list1)
    print('the summary of numbers is',summary(numbers))
    pass

def lesson13(): #13: Positional, Keywords & Default Arguments in Python
    def function(x = 5):
        print(x)
    function()
    function(6)
    #def function(x = 1, y) !! all the arguments has to be with or without defaul value
    def function(x, y):
        print(x,y)
    #function() !! need a values
    #function(6) !! need all 2 values
    function(2,3)
    pass

def lesson14(): #14: Python Local & Global Variables
    def function():
        result=1 #this variable works only in funcion
    #print(result) !! theres no variable in the program
    text = 'first'
    def function():
        global text
        #print(text) - dlaczego nie działa ???
        text = 'second'
        print(text)
    function()
    pass

def lesson15(): #15: Lists & Tuples in Python
    l1 = []
    l2 = [1,2,3,4,5] #indexing is 01234 or -5-4-3-2-1
    print(l1,len(l1),l2,len(l2))
    print(l2[1],l2[4],l2[-1],l2[0],l2[-3])
    print(l2[2:3],l2[1:],l2[:3])
    l2[2:4] = [33,44]
    print(l2)
    print(2 in l2) #print True if 2 is in list l2
    l2.append(6) #adding 6 as the next element of list
    print(l2)
    l2.insert(1, 1.5) #adding 1.5 as the first element of a list - the following indexes go +1
    print(l2)
    l2.remove(1.5) #removing element of a list
    print(l2)
    l3 = l2.copy() #copying list
    print(l3)
    numbers = (1,2,3,4,5,6) #its not a list, its a tuple
    print([1,2,3,4,5,6],numbers)
    #numbers[0]=11 !! you cannot change the value from tuple
    pass

def lesson16(): #16: Python Strings (Textual Data)
    print('Hello')
    print('''Hello
    Hello''') #this tab will be written
    text = 'Python'
    #text[0]='p' !! you cannot change characters in string
    print(text * 3) #PythonPythonPython
    print(text.upper()) #PYTHON
    print(text.lower()) #python
    print(text.find('y')) #1 - index of y
    print(text.find('th')) #2 - index of first letter, t
    print(text.replace('hon','HON')) #PytHON
    pass

def lesson17(): #17: Python Dictionaries to Store key/value Pairs
    person1 = {
        'name': 'Linus',
        ('age'): 21,
    }
    print(person1) #{'name': 'Linus', 'age': 21}
    print(person1['name'],person1['age']) #Linus 21
    print(person1.get('hobbies')) #none
    print(person1.get('hobbies', 'No keys like hobbies')) #No keys like hobbies
    print(person1.get('name')) #Linus
    person1['name'] = 'Dennis'
    print(person1) #{'name': 'Dennis', 'age': 21}
    person1['hobbies'] = ['dancing', 'fishing']
    print(person1) #{'name': 'Dennis', 'age': 21, 'hobbies': ['dancing', 'fishing']}
    person1.pop('name') #to remove a key
    print(person1) #{'age': 21, 'hobbies': ['dancing', 'fishing']}

    for key in person1:
        print(key)
        print(person1[key])
    pass

def lesson18(): #18: Sets in Python
    #items in sets are 1.unique 2.not ordered 3.constant
    animals = {'dog','cat','tiger','elephant'}
    print(animals) #{'tiger', 'cat', 'dog', 'elephant'} - randomly
    animals = {'dog','cat','tiger','elephant','dog'}
    print(animals) #the same like before
    animals = set()
    print(animals) #set() - empty set
    animals = set(['c','b','f','j'])
    print(animals) #{'j', 'f', 'c', 'b'} - list changed into set
    
    animals.add('r')
    print(animals) #{'b', 'j', 'f', 'r', 'c'} - added r
    animals.update('p','r',{'k'})
    print(animals) #{'k', 'j', 'c', 'f', 'r', 'p', 'b'} - added p and k, but r stayed
    animals.remove('p')
    print(animals) #{'f', 'j', 'k', 'b', 'c', 'r'} - removed p
    #animals.remove('u') !! you cannot remove non existing elements of set
    animals.clear()
    print(animals) #set() - set emptyed
    
    animals = {'dog','cat','tiger','elephant'}
    print('tiger' in animals) #True
    domestic_animals = {'dog','cat','parrot'}
    wild_animals = {'tiger','elephant','parrot'}
    animals = wild_animals.union(domestic_animals) #you can swipe variables
    print(animals) #{'elephant', 'cat', 'dog', 'tiger', 'parrot'}
    animals = wild_animals.intersection(domestic_animals) #you can swipe variables
    print(animals) #{'parrot'} - only animals present in both sets
    pass

def lesson19(): #19: Python Range Function
    result = range(1, 11) #range(0,10) === range(10)
    print(result)
    print(list(result))
    for value in range(1,6):
        print(value, 'number')
    
    result = range(1,11,2) #2 - step by 2 numbers
    print(list(result))
    result = range(11,1,-1) #decreasing
    print(list(result))
    print (list(range(3,31,3)))
    pass

def lesson20(): #20: Object-oriented Programming (OOP) in Python
    class Student:
        def check_pass_fail(self):
            if self.marks >= 40:
                return True
            else:
                return False
        pass
    
    student1 = Student()
    student1.name = 'Harry'
    student1.marks = 85
    did_pass = student1.check_pass_fail()
    print(student1.name)
    print(student1.marks)
    print(did_pass)

    student2 = Student()
    student2.name = 'Janet'
    student2.marks = 30
    did_pass = student2.check_pass_fail()
    print(student2.name)
    print(student2.marks)
    print(did_pass)
    print('')

    class Student:
        def check_pass_fail(self):
            if self.marks >= 40:
                return True
            else:
                return False
        def __init__(self,name,marks):
            self.name = name
            self.marks = marks
    student1 = Student('Tom',85)
    print(student1.name)
    print(student1.marks)
    student2 = Student('Juliette',30)
    print(student2.name)
    print(student2.marks)

    class Complex:
        def __init__(self,real,imag):
            self.real = real
            self.imag = imag
        def add(self, number):
            real = self.real + number.real
            imag = self.imag + number.imag
            result = Complex(real, imag)
            return result
    n1 = Complex(5,6)
    n2 = Complex(-4,2)
    result = n1.add(n2)
    print('real =',result.real)
    print('image =',result.imag)
    
    pass

def lesson21(): #21: Everything is an Object in Python!
    numbers = [1,4,9,16]
    print(type(numbers))
    n1 = 5
    print(type(n1))
    flag = True
    print(type(flag))
    def function():
        pass
    print(type(function))

    numbers = [1,2]
    print(dir(numbers))
    result = numbers.__add__([3,4]) #the same as: numbers + [3,4]
    print(result)

    number1, number2 = 5, 10
    print(id(number1),id(number2))

    a = [1,2,3]
    b=a
    a.append(4)
    print(a,b) #[1, 2, 3, 4] [1, 2, 3, 4] - a and b are referent to the same object
    print(id(a),id(b))

    a = [1,2,3]
    b=a.copy()
    a.append(4)
    print(a,b) #[1, 2, 3, 4] [1, 2, 3] - a and b dont have the same id
    print(id(a),id(b))

    pass

def lesson22(): #22: Inheritance in Python (Derived/Child Classes)
    class Animal:
        def eat(self):
            print('I can eat')
    class Dog(Animal): #class Dog inheritances class Animal
        def bark(self):
            print('I can bark')
    class Cat(Animal):
        def get_grumpy(self):
            print('I am getting grupmy')
    dog1 = Dog()
    dog1.bark() #I acn bark
    dog1.eat() #I can eat
    cat1 = Cat()
    cat1.eat() #I can eat

    class Polygon:
        def __init__(self, sides):
            self.sides = sides

        def display_info(self):
            print("A polygon is a two dimensional shape with straight lines")

        def get_perimeter(self):
            perimeter = sum(self.sides)
            return perimeter
    
    class Triangle(Polygon):
        def display_info(self):
            print("A triangle is a polygon with 3 edges")
            Polygon.display_info(self) #ptints display_info from Triangle, and then from Polygon
            super().display_info() #the same as above, cant leave 'self', because super() is an object, not a class

    class Quadrilateral(Polygon):
        def display_info(self):
            print("A quadrilateral is a polygon with 4 edges")
    
    t1 = Triangle([5,6,7])
    perimeter = t1.get_perimeter()
    print('The perimeter is',perimeter)
    t1.display_info() #method names from derived class have priority

def lesson23(): #23: Import, Use & Create Modules in Python
    def basic_import():
        import math
        number = 25
        print(math.sqrt(number))
        print(math.pi)
    basic_import() 
    def import_as_variable():
        import math as m
        number = 25
        print(m.sqrt(number))
        print(m.pi)
    import_as_variable()
    def import_specific_methods():
        from math import sqrt, sin, pi #to import all type "*"
        print(sqrt(64))
        print(sin(pi/2))
    import_specific_methods()
    import math
    print(dir(math))

    #Custom module - calculator (in this directory)
    import calculator as c
    print(c.add(2,3))
    print(c.multiply(2,3))

def lesson24(): #24: Python Packages & pip (package manager)
    #Look for dorectory: "pfb24"
    pass

def lesson25(): #25: Python Exception Handling: try...catch...finally
    numerator = 10
    denominator = 0
    try:
        print(numerator/denominator) #!! you cant divide by 0
    except ZeroDivisionError: #only when dividing by 0 occour
        print("Division by 0, try again")
    print('end')
    #print the error
    #except Exception as e:
    #   print("e")

    try:
        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))

        result = numerator/denominator
        print(result)
    
        my_list = [1, 2, 3]
        i = int(input("Enter index: "))
        print(my_list[i])
    except ZeroDivisionError:
        print("Denominator cannot be 0. Try again.")
    except IndexError:
        print("Index is wrong.")
    print("Program ends")

    try:
        print(1/0)
    except:
        print("Division by 0")
    finally:
        print('Always will be printed')

def lesson26(): #26: Python File Handling: Create, Read & Write Files
    try:
        f = open("message.txt", "r") #r -read, w - write, a - adds at the end of file, creates new file
        content = f.read(6)
        print(content) #I love

        more_content = f.read(12) # programming (with space at the beggining)
        print(more_content)
    except:
        print("error")
    finally:
        f.close()

    with open("message.txt","r") as f: #use it instead of basic formula
        content = f.read(6)
        print(content) #I love
        more_content = f.read(12)
        print(more_content) # programming

    with open("text.txt","w") as f:
        f.write("Python is awesome\n")
        f.write("I love Python")

    with open("text.txt","a") as f:
        f.write("\nPython is awesomeeee")
    
    with open("text.txt","r") as f:
        lines = f.readlines() #puts lines from .txt to list named "lines"
        print(lines)

    with open("text2.txt","w") as f:
        lines = ['JS is awesome','\nJS is second']
        f.writelines(lines) #puts list named "lines" to lines in file
    pass

def lesson27(): #27: Python os Module (Work with Directories)
    import os
    current_dir = os.getcwd()
    print(current_dir)
    #os.chdir("D:\directory") - changes the location of this file to this path
    #print(os.listdir())
    #os.mkdir("test") #mkdir test
    #os.mkdir("test/test2") #mkdir test2 inside dir test
    #os.rename("test","test-new") #renaming test

    #print(os.listdir())
    #os.remove("text.txt") #removing text.txt
    #print(os.listdir())

    #print(os.listdir())
    #os.rmdir("test-new/test2") #rmdir test-new/test2
    #print(os.listdir())

    #print(os.listdir())
    #os.rmdir("test-new") #rmdir test-new
    #print(os.listdir())
    pass

def lesson28(): #28: Iterators in Python
    numbers = [1,4,9]
    print(dir(numbers))

    value = numbers.__iter__()
    print(value) #<list_iterator object at 0x0000020C8F155F60>

    value = numbers.__iter__()
    item1 = value.__next__()
    item2 = value.__next__()
    item3 = value.__next__()
    print(item1,item2,item3) #1 4 9

    value = iter(numbers)
    item1 = next(value)
    item2 = next(value)
    item3 = next(value)
    print(item1,item2,item3) #1 4 9

    iter_obj = iter(numbers)
    while(True):
        try:
            element = next(iter_obj)
            print(element)
        except StopIteration:
            break
    
    class Even:
        def __init__(self, max):
            self.n = 2
            self.max = max
        def __iter__(self):
            return self
        def __next__(self):
            if self.n <= self.max:
                result = self.n
                self.n += 2
                return result
            else:
                raise StopIteration
    numbers = Even(10)
    print("")
    print(next(numbers))
    print(next(numbers))
    print(next(numbers))
    pass

def lesson29(): #29: Generators in Python: How to Use them & Why?
    def even_generator():
        n=0
        n += 2
        yield n #n=2
        n += 2
        yield n #n=4
        n += 2
        yield n #n=6
        pass

    numbers = even_generator()
    print(next(numbers)) #first yield
    print(next(numbers)) #second yield
    print(next(numbers)) #third yield
    
    def even_generator(max):
        n=2
        while n <= max:
            yield n
            n += 2  

    numbers = even_generator(4) #generating for numbers up to 4
    print("")
    print(next(numbers)) #first yield
    print(next(numbers)) #second yield

    numbers = even_generator(5) #generating for numbers up to 5
    print("")
    print(next(numbers)) #first yield
    print(next(numbers)) #second yield

    #infinite stream of data
    def generate_fibonacci():
        n1 = 0
        n2 = 1
        while True:
            yield n1
            n1, n2 = n2, n1 + n2
    
    seq = generate_fibonacci()
    for i in range(6):
        print("1 number of fibonacci:",next(seq))

    pass

def lesson30(): #30: Working with Python date & time (datetime module)
    import datetime as dt

    print("DATE")
    current_date = dt.date.today()
    print("Current date:",current_date)
    date1 = dt.date(2021,1,5)
    print(date1,"\t",date1.year,date1.month,date1.day)
    print("")

    print("TIME")
    #current_time - my idea)
    # now = dt.now()
    # current_time = now.strftime("%H:%M:%S")
    # print("Current Time:", current_time)
    time1 = dt.time(10,45,30,123456) #max 6 digits in last parameter
    print(time1,"\t",time1.hour,time1.minute,time1.second,time1.microsecond)
    print("")

    print("DATETIME")
    current_datetime = dt.datetime.now()
    print("Current Datetime:",current_datetime)
    datetime_obj = dt.datetime(2021,11,28,23,55,59) #datetime = date + time
    print(datetime_obj,"\t",datetime_obj.date(),datetime_obj.time())
    print("")

    current_datetime = dt.datetime.now()
    next_new_year = dt.datetime(2022,1,1)
    time_remaining = next_new_year - current_datetime
    print(time_remaining)
    print(type(time_remaining))
    print("")

    current_datetime = dt.datetime.now()
    print(current_datetime)
    string_date = current_datetime.strftime("%A, %B, %d, %Y") #changed format of current_datetime
    #Code list for strftime: https://www.programiz.com/python-programming/datetime/strftime
    print(string_date)
    print("")

    date_string = "21 June, 2021"
    date_object = dt.datetime.strptime(date_string, "%d %B, %Y") #new object from declared format of date_string
    print(date_object)
    pass

def lesson31(): #31: Python Decorators
    def inc(x):
        return x + 1
    def operate(func,x): #func is a function assigned to function inc
        result = func(x)
        return result
    print(operate(inc,3))

    #Decorators - pojebane to jakieś
    def printer():
        print("Hello")
    def display_info(func):
        def inner():
            print("Executing", func.__name__,"function")
            func()
            print("Finished execution")
        return inner
    
    decorated_func = display_info(printer)
    decorated_func()
    print("")

    print("Executing", decorated_func.__name__,"function") #Executing inner function - not decorated_func
    decorated_func()
    print("Finished execution")
    print("")

    @display_info
    def printer():
        print("Hello world!")
    printer()

    #Decorating functions with parameters
    def smart_divide(func):
        def inner(a,b):
            print("Dividing",a,"by",b)
            if b == 0:
                print("Cant divide by 0")
                return
            return func(a,b)
        return inner
    
    @smart_divide
    def divide(a,b):
        return a / b
    
    value1 = divide(15,3)
    print(value1)
    value2 = divide(15,0)
    print(value2)
    pass

    def star(func):
        def inner(arg):
            print("*" * 30)
            func(arg)
            print("*" * 30)
        return inner

    def percent(func):
        def inner(arg):
            print("%" * 30)
            func(arg)
            print("%" * 30)
        return inner

    @star
    @percent
    def printer(msg):
        print(msg)

    printer("Decorators are wonderful")

#lessonX() - X is number of lesson
lesson30()