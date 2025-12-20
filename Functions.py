# Defining a function
# def Test():
#     return ("Hello Venkat")
# #     Calling a function
# print(Test())
# returning function (return value)
# def Test():
#     a = 5
#     b = 6
#     return a, b
# print(Test())
# def add(x, y):
#     return x + y
# def apply(function, x, y):
#     return function(x, y)
# result = apply(add, 9, 9)
# print(result)

# Formal arguments(parameter) and Actual arguments
# def f1(x, y):
#     return x + y
# print(f1(4, 8))

# def my_function(my_list):
#     my_list.append(10)
# l1 = [25, 27, 39]
# print(l1)
# my_function(l1)
# print(l1)

# Arbitary arguments
# def my_function(*name):
#     print ('Hello', name)
# my_function('A', 'B', 'C', 'D')
# my_function('A', 'B', 'C','D','E','F','G')

# def my_function(**details):
#     for key, values in details.items():
#         print(key, values)
# my_function(name="saran", surname="Venkat", age=21, height=4.8)

# Global
# x = 10
# print(x)
# def f1():
#     print(x)
# f1()

# Recursion
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))

# Lambda arguments: expression
# a = lambda x: x + 5
# print(a(10))

# power of lambda
# def power(n):
#     return lambda a: a ** n
# square = power(2)
# cube = power(3)
# print(square(2))
# print(cube(3))

# Decorators
# def my_decorator(func):
#     def wrapper():
#         print('something is happening Before the function is called')
#         func()
#         print('something is happening After the function is called')
#     return wrapper
# @my_decorator
# def say_hello():
#     print('Hello')
# say_hello()
# decorated = my_decorator(say_hello)
# decorated()

# Generators
# def fibo(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a+b
#
# x = fibo(4)
# print(next(x))
# print(next(x))
# print(next(x))

# Modulus
# structured programming
# import Modules as m
# from Modules import *
# f1()
# square = power(2)
# print(square(2))


# input() Takes string as a input
# user = float(input("Enter value:"))
# print(user)
# print(type(user))

# Map()
# collec = [10, 25, 43, 19, 16]
# collec2 = list(map(float, collec))
# double = list(map(lambda x: x * 2, collec))
# print(double)

# Filter
age = [15, 57, 26, 28, 30, 10, 15, 19, 12, 9, 7]
def children(x):
    return x >= 15
#         return True
#     else:
#         return False
children = list(filter(children, age))
print(children)
