# Exercise:conversion of weight (lbs to kg)
weight = input('Enter weight(in pounds): ')
in_kilos = 0.45 * int(weight)  # Casting is done using constructor function, e.g. int()
print(in_kilos)
print(type(in_kilos))

# Slicing

course = "Python for beginners"
print(course[0:2])   # o/p-  Py
print(course[-1])    # o/p-  s
print(course[0:])    # o/p-  Python for beginners
print(course[1:])    # o/p- ython for beginners
print(course[:5])    # o/p- Pytho
print(course[:])     # o/p- Python for beginners (copy)
print(course[1:-1])  # o/p- ython for beginner
print(course[-5:-2])  # o/p- nne (slice from end of the string)

# Formatted strings

first, last = 'John', 'Smith'
# string concatenation : we cannot concatenate a string and an integer(TypeError!)
message = first + ' [' + last + '] is a coder'
# formatted string : {}=placeholders
msg1 = f'{first} [{last}] is a coder'
print(msg1)
msg2 = "{0} [{1}] is a coder"   # OR
print(msg2.format(first, last))

# Membership operators : 'in' and 'not in' operator
print('Python' in course)   # o/p-True

a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)

x = 10
x += 3  # Augmented assignment operator or enhanced assignment operator

x = 10 + 3 * 2 ** 2  # 22

# Exercise 1:conditional statement
price_of_house = 1000000
good_credit = False
if good_credit:
    down_payment = price_of_house * 0.1
else:
    down_payment = price_of_house * 0.2
print(f"Down Payment: ${down_payment}")

# Exercise 2:
name = input()
if len(name) < 3:
    print("Name Must be at least 3 characters long.")
elif len(name) > 50:
    print("Name can be maximum of 50 characters.")
else:
    print("Name looks good!")

# Exercise 3:
weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")
value1 = 'l' or 'L'
value2 = 'k' or 'K'
if unit == value1:
    print(f"You are {weight * 0.45} kilos.")
elif unit == value2:
    print(f"You are {weight / 0.45} pounds.")
else:
    print("Invalid input!")
# Alternate method is to use built-in string methods i.e.
if unit.upper() == "L":
    print("This is in pounds")
else:
    print("This is kilos")

# while loops
i = 1
while i <= 5:
    print('*' * i)
    i += 1
print("Done")

'''
No i++(i.e. increment operator) in Python, cause integers in Python are 'immutable'. 
You can reassign it but you can not increment it.
> Python uses names and objects.
i = 1  , here 1 is the value of object of type int, bound with name 'i'
i = i + 1 
'''

# Guessing game:
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed!")

# Car game:
event = ""
event0 = 'help'
event1 = 'start'
event2 = 'stop'
event3 = 'quit'
started = False
while True:
    event = input("> ").lower()
    if event == event1:
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started...ready to go.")
    elif event == event2:
        if not started:
            print("Car already stopped!")
        else:
            started = False
            print("Car stopped.")
    elif event == event0:
        print("start-to start the car\nstop-to stop the car\nquit-to exit")
    elif event == event3:
        break
    else:
        print("I don't understand that...")

# For loop:
total = 0
prices = [1, 2, 3, 4, 5]
for items in prices:
    total = int(total) + items
print(total)

'''
Challenge:Using nested loop print
xxxxx
xx
xxxxx
xx
xx
'''
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

# List: find maximum no. in list
numbers_list = [1, 2, 3, 10, 5]
maximum = numbers_list[0]
for x in numbers_list:
    if x > maximum:
        maximum = x
print(maximum)

