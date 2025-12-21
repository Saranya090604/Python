# List : Square brackets
# ordered, changeable, and Allow duplicates
# l1 = ['a','b','c']
# l2 = [1 , 9, 10]
# l3 = [True, False, True, False]
# l4 = ['s', 'v', 5, 8, 9.2, 8j, True, False]
# print(l1, l2, l3, l4, sep='\n')
# print(type(l1), type(l2), type(l3), type(l4), type(l4), sep='\n')

# l1 = list(range(15))
# print(l1)
#
# l2 = list(range(5, 15))
# print(l2)
#
# l3 = list(range(6, 13, 2))
# print(l3)

# l1 = [10, 39, 46, 37, 63, 50]
# print(l1[1:5])
# print(l1[:4])
# print(l1[::3])
#
# # update
# l1 = [10, 39, 46, 37, 63, 50]
# print(l1)
# l1[3] = 'Saranya'
# print(l1)
#
# l1 = [10, 39, 46, 37, 63, 50]
# print(l1)
# l1[2:4] = ['Hello', 'Saranya']
# print(l1)

# l1 = [1,2,3,4,5,6,7,8,9]
# print(l1)
# #append
# l1.append('kiwi')
# print(l1)
# l1.insert(5, 'Mango')
# print(l1)
# l2 = [25, 46]
# l1.extend(l2)
# print(l1)
#
# l1 = [2, 5]
# l2 = [9, 10]
# for x in l2:
#     l1.append(x)
#     print(l1)

# l1 = [1, 2, 3, 4, 5, 'Mango', 6, 7, 8, 9, 'kiwi', 25, 46]
# print(l1)
# l1.pop(6)
# print(l1)
# del l1[3:8]
# print(l1)
# l1.clear()
# print(l1)

l1 = ["Apple", "Kiwi", "Cherries", "Oranges", "avacado"]
print(l1)
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
