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

# l1 = ["Apple", "Kiwi", "Cherries", "Oranges", "avacado"]
# print(l1)
# l1.sort()
# print(l1)
# l1.sort(reverse=True)
# print(l1)

# max and min
# l1 = [10, 20, 30, 40, 50, 60, 70, 80]
# print(max(l1))
# print(min(l1))
#
# # membership
# print(40 in l1)
# print('saranya' not in l1)
#
# # nested list
# l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(l1)
# l2 = [10, 11, 12]
# l2.append(l1)
# print(l1)

# List comphrension

# names = ['anna', 'john', 'rosy', 'ananya', 'lavanya']
# names_with_a = [all_items for all_items in names if 'a' in all_items]
# print(names_with_a)
#
# double_from_0_5 = [number for number in range(5)]
# print(double_from_0_5)


# matrix
matrix = []
for i in range(4):
    matrix.append([])
    for j in range(4):
        matrix[i].append(j)
    print(matrix)

matrix =[[y for y in range(4)] for x in range(4)]
print(matrix)

# Tuples

t1 = (10, 20, 30, 40, 50)
print(t1)
t2 = ('anu', 'aksha', 'kaviya')
t3 = (True, False, False, True)
t4 = (10, 20, 30, 40,'anu','aksha',True, False, False)
print(t1, t2, t3, t4, sep='\n')
print(type(t1), type(t2), type(t3), type(t4), type(t4), sep='\n')

# * -> means remaining all items
t1 = ('A', 'B', 'C', 'D', 'E', 'F')
print(t1)
a, *b, c = t1
print(a)
print(b)
print(c)