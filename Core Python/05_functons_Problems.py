# Returns Square
# def square(number):
#     return number**2

# print(square(2))

# Functons with multiple parameters
#create a function that takes two parameters as input and return there sum
# def add(num1,num2):
#     return num1+num2
# print (add(1,1))

# Polymorphism in function 
# Polymorphism in Python means using the same function or method name for diffrent operations

# def Multiply(a,b):
#     return a*b
# print(Multiply(2,5))
# print(Multiply(2,'a'))
# area of circle
# import math
# def areaofcircle(radius):
#     area=math.pi*radius ** 2
#     circum=2 * math.pi * radius
#     return area,circum
# a,c=areaofcircle(3)
# print(a,c)

# write a function to greet a user 

# def greet(name):
#     return "hello " + name 
# print(greet("Pratham"))

# lambda function for cube

# cube=lambda x:x**3
# print(cube(3))

# # *args lets you pass multiple values to a function without listing them one by one in the definition.
# def add_numbers(*args):
#     return sum(args)

# print(add_numbers(1, 2, 3, 4))

# A decorator is a special function that adds extra features to another function 
# without changing its code.

def greet_decorator(func):
    def wrapper():
        print("Hello!")
        func()
        print("Goodbye!")
    return wrapper
@greet_decorator
def say_name():
    print("My name is Pratham")

say_name()



