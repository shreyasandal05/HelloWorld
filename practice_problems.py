# All parameters(arguments) in python are passed by reference.
# Means: if you change what a parameter refers to within a function, the change reflects back in calling function.
# def change_my_list(list1):
#     """Changes passed list into this function"""
#     print("value inside function before change:", list1)
#     list1[2] = 50
#     print("value inside function after change:", list1)
#     return
#
#
# list1 = [10, 20, 30]
# change_my_list(list1)
# print("value outside the function:", list1)
'''
o/p-
value inside function before change: [10, 20, 30]
value inside function after change: [10, 20, 50]
value outside the function: [10, 20, 50]
'''
# properties = ["big", "small", "bold", "light", "heavy"]
# materials = ["iron", "silver", "gold", "platinum", "diamond"]
# a = 0
# b = 0
# for i in properties:
#     for j in materials:
#         print(x[a], y[b])
#         b += 1
#     a += 1
#     b = 0
#
# pizza = ["NY style pizza", "Pan Pizza", "Thin n crispy pizza", "stuffed crust pizza", "Pizza"]
# # choice = 'Pan Pizza'
# for choice in pizza:
#     if choice == "Pan Pizza":
#         print("Please pay $16.Thank you.")
#     print("Delicious cheesy " + choice)
# else:
#     print("Cheesy pan pizza is my favorite")
# print("Finally, I'm full!")
# '''
# o/p-
# Delicious cheesy NY style pizza
# Please pay $16.Thank you.
# Delicious cheesy Pan Pizza
# Delicious cheesy Thin n crispy pizza
# Delicious cheesy stuffed crust pizza
# Delicious cheesy Pizza
# Cheesy pan pizza is my favorite
# Finally, I'm full!
# '''

# x = 10
# total = 0
# for number in range(1, 50+1):
#     total = total + number
# print(total)

Even = int(input("Enter the input"))
total = 0
for number in range(1, Even+1):
    if number % 2 == 0:
        print(number)
        total = total + number
print("The sum of even numbers", total)
