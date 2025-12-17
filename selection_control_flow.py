# One way selection
# order = 250
# minimum_order = 200
# delivery_charge = 30

# if order < minimum_order:
#     delivery_charge = 50

# total_cost = order + minimum_order + delivery_charge
# print(total_cost)

# Two way selection
# marks = 100
# pass_mark = 50

# if marks < pass_mark:
#     print("you have passed")
#     print("Congratulations!")
# else:
#     print("you have failed")
#     print("sorry! Better than next time")

# Multi way selection
# marks = 10
# if marks < 30:
#     print("positive")
# elif marks == 30:
#     print("zero/non negative")
# else:
#     print("negative")

# short Hand if....else
# a = 30
# print("Greater than 20") if a > 40 else print("Not Greater than 20")

# Logical operator and or not
# AND (Both condition satisfied)
# a = 69
# b = 90
# c = 25
# if a > b and c > a:
#     print("Condition is true")
# else:
#     print("Condition is false")

# OR (Any one condition satisfied)
# a = 69
# b = 90
# c = 25
# if c <= a or b == a:
#     print("Condition is true")
# else:
#     print("Condition is false")

# not (opp)
# if not(True):
#     print("True")
# else:
#     print("False")

number = 50
if number > 45:
    print("Condition is true")
    if number < 70:
        print("oops")
    else:
        print("good luck")
else:
    print("Condition is false")

