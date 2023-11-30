# 11.Write a program that checks whether an input number is a palindrome or
# not.

def is_palindrome(number):
    str_number = str(number)

    return str_number == str_number[::-1]


num = int(input("Enter a number: "))

if is_palindrome(num):
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")
