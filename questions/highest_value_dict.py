#
# 27. Write a Python program to find the highest 2 values in a dictionary.


employee_salaries = {'John': 50000, 'Jane': 60000, 'Bob': 55000}

highest_salaries = sorted(employee_salaries.values(), reverse=True)[:2]

print("Highest 2 salaries:", highest_salaries)
