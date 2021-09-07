import random
import converters
from converters import kg_to_lbs
from utils import find_max
from ecommerce.shipping import calc_shipping

# Functions:

# Positional argument- position of arguments gives value of parameters


def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("welcome")


print("start")
greet_user("John", "Smith")

# Keyword argument- position doesn't matter
# use keyword argument when dealing with lots of numbers otherwise positional argument.
# if you are passing both positional and keyword argument use keyword argument after positional argument only.

greet_user("Mary", last_name="Smith")
print("Finish")

# Emoji converter


def emoji_converter(message):
    new_msg = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "🙁",
        ":/": "😕",
        "^_^": "☺",
        ";)": "😉",
        ":P": "😜"
    }
    output = ''
    for word in new_msg:
        output += emojis.get(word, word) + " "
    return output


print(emoji_converter(input(">")))

# Error handling

try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age cannot be 0")

# Classes- we use classes to define new types
# These types can have different methods that we define in the body of the class
# self- reference to current instance of class


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Move.")

    def draw(self):
        print("draw.")


point1 = Point(10, 20)  # Instantiation
point1.x = 10  # object can have different attributes
point1.y = 20
print(point1.x)
point1.move()


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


men = Person("john")
men.talk()

# Inheritance


class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass


class Cat(Mammal):
    def be_annoying(self):
        print("annoying.")


dog = Dog()
dog.walk()
cat = Cat()
cat.be_annoying()

# Modules- we use modules to better organise our code. It contains all related functions and classes

# For example:1.
print(kg_to_lbs(70))
print(converters.lbs_to_kg(155))
# 2
numbers = [10, 2, 3, 5, 6]
find_max(numbers)
# 3
calc_shipping()

# Exercise:Generate random numbers


class Dice:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def roll(self):
        return print(f"({self.first_num},{self.second_num})")


numbers = (1, 2, 3, 4, 5, 6)
dice = Dice(first_num=random.choice(numbers), second_num=random.choice(numbers))
dice.roll()

# Alternate method:


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second  # automatically interprets as a tuple


dice = Dice()
print(dice.roll())
