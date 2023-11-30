#  Q35. Write a python program to find out the sum and average of numbers in a
# list


def calculate_sum_and_average(numbers):
    sum_of_numbers = sum(numbers)
    average_of_numbers = sum_of_numbers / len(numbers)
    return sum_of_numbers, average_of_numbers


my_numbers = [10, 20, 30, 40, 50]
sum_result, average_result = calculate_sum_and_average(my_numbers)
print(f"Sum Of numbers: {sum_result}")
print(f" Average Of numbers: {average_result}")
