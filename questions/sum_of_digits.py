# 15.Input a string having some digits. Write a program to return the sum of
# digits present in this string

def sum_of_digits(input_string):
    total = 0
    for char in input_string:
        if char.isdigit():
            total += int(char)
    return total


print(sum_of_digits("shiv123"))
