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
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))