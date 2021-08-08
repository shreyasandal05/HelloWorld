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
