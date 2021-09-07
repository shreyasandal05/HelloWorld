def find_max(numbers):
    """This prints maximum number within a list"""
    maximum = numbers[0]
    for number in numbers:
        if maximum < number:
            maximum = number
    print(maximum)
