# 5. Write a program that asks the user to enter their name and age. Print a
# message addressed to the user that tells the user the year in which they
# will turn 100 years old.

def calculate_age(number):
    current_year = 2023
    turn_100 = current_year + (100 - age)
    return turn_100


name = input("Enter name: ")
age = int(input("Enter age: "))

year_100 = calculate_age(age)
print(f"Hello, {name}! You will turn 100 years old in this year :{year_100}.")
