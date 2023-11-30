# 22. Write a program for finding the maximum, minimum and mean of
# numeric values stored in a tuple

def calculate_stats(numbers):
    max_value = max(numbers)
    min_value = min(numbers)
    mean_value = sum(numbers) / len(numbers)
    return max_value, min_value, mean_value


# Create a tuple of numbers
my_numbers = (10, 20, 30, 40, 50)

# Get the results
max_num, min_num, mean = calculate_stats(my_numbers)

# Print the results
print("Maximum:", max_num)
print("Minimum:", min_num)
print("Mean:", mean)
