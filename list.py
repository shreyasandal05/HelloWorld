# 2d lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)   # o/p- 1 to 9 (one on each line)

# List methods:
numbers = [5, 2, 1, 4, 7]
numbers.append(13)
# similarly,
# insert(index:0,object:10)  o/p-[10, 5, 2, 1, 4, 7]
# remove(5)  o/p-[2, 1, 4, 7]
# clear()  o/p-[]
# sort()
# reverse()
# pop() :removes last item in the list i.e. '4'
# index(5) :index of first occurrence of an element, here '0'
# count(5): counting no. of occurrence of an item o/p-1
print(numbers)
print(numbers.sort())  # o/p- None
# None is an object in python that represents absence of a value like null
print(50 in numbers)  # 'in' operator:Checks if element is present in the list o/p-False

# All about None:


def no_return():
    pass


no_return()
'''
Here, function returns a None type under the hood.
In fact, print() itself has no return value(i.e returns None)
'''
print(no_return())   # o/p- None [print() returns None but we don't see it]
print(print(no_return()))  # o/p- None\nNone
x = [1]
y = [1]
print(x == y)  # o/p- True
print(x is y)  # o/p- False
print(id(x))
print(id(y))   # different ids
# whereas....
x = None
y = None
print(x == y)   # o/p-True
print(x is y)   # o/p-True
'''
This is because there is only one None in Python.
None is singleton.
'''
# confirmation:
print(id(x))
print(id(y))  # same ids
# NOTE:
'''
 is faster than '==' operator
'''

# program to remove duplicates in a list

numbers = [5, 1, 5, 3, 2, 1, 1, 2, 1, 7, 7]

# doesn't work:/
# numbers.sort()
# for i in numbers:
#     if numbers.count(i) > 1:
#         numbers.remove(i)
# print(numbers)

# working method:

unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)

# Tuple

numbers = (1, 2, 3)
print(numbers[0])   # o/p - 1
# numbers[0] =10   # o/p-TypeError

# unpacking

coordinates = (1, 2, 3)  # similarly with lists
x, y, z = coordinates
print(x)  # o/p-1

# Dictionary:

customers = {
    "name": "Light Yagami",
    "age": 30,
    "is_verified": True
}
customers["birthdate"] = "Jan 5 1997"
print(customers["birthdate"])

# Exercise
phone = input("Phone: ")
phone_dictionary = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five"
}
output = ""
for i in phone:
    output += phone_dictionary.get(i, "!") + " "
print(output)

# Emoji converter
message = input(">")
new_msg = message.split(" ")
emojis = {
    ":)": "😊",
    ":(": "🙁",
    ":/": "😕",
    "^_^": "☺",
    ";)": "😉",
    ":P": "😜"
}
output = ""
for word in new_msg:
    output += emojis.get(word, word) + " "
print(output)
