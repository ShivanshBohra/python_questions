# 18.Write a program for finding the maximum, minimum and mean of
# numeric values stored in a list


def analyze_numeric_values(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    mean = sum(numbers) / len(numbers)
    return maximum, minimum, mean


input_numbers = input("Enter number list: ")
number_list = [float(num) for num in input_numbers.split()]
print(analyze_numeric_values(number_list))
