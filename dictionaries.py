# d1 = {
#     'Name': 'saranya',
#     'Age': 21,
#     'Gender': 'Female',
#     'car': ['BMW', 'BENZ'],
#     'Name': 'sanjana'
# }
# print(d1)
# print(type(d1))
# print(len(d1))
# print(d1['Name'])

# d1 = {
#     'Name': 'john',
#     'Age': 20,
#     'car': 'BMW',
#     "Year": 2012,
#     'Married': True,
# }
# print(d1)
# d1['Year'] = 2024
# print(d1)
#
# d1.update({'Year': 2025})
# print(d1)

d1 = {
    'Name': 'john',
    'Age': 20,
    'car': 'BMW',
    "Year": 2012,
    'Married': True,
}
for x in d1:
    print(x)
    print(d1[x])

# sorting of dictionaries
d1 = {'a': 4, 'b': 6, 'c': 2, 'd': 1}
x = dict(sorted(d1.items(), key=lambda item: item[1]))
print(x)
