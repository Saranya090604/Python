# Iterations
# while : executes a set of statement as long as a condition is true
# i = 2
# while i <= 7:
#     print(i)
#     i += 1
# stop: break
# while i <= 10:
#     print(i)
#     if i == 4:
#         break
#     i += 1
# while i <= 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
# For Loop
# l1 = ["Apple", "strawberry", 25, "Orange"]
# for each_item in l1:
#     print(each_item * 2)

# text = "Hello Saranya"
# for each_word in text:
#     print(each_word)

l1 = [10, 12, 25, 20]
for each_number in l1:
    if each_number == 12:
        continue
    print(each_number * 2)
else:
    print("Good bye")
