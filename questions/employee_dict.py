# 26. Write a program to create a dictionary with names of employees, their
# salary and access them

def create_employee_dict(names, salaries):
    employee_data = dict(zip(names, salaries))
    return employee_data


def access_employee_salary(employee_data, employee_name):
    if employee_name in employee_data:
        return employee_data[employee_name]
    else:
        return f"No salary information found for {employee_name}"


employee_names = ['John', 'Jane', 'Bob']
employee_salaries = [50000, 60000, 55000]

employee_dict = create_employee_dict(employee_names, employee_salaries)

print("Employee Dictionary:", employee_dict)

employee_to_check = 'Jane'
print(f"{employee_to_check}'s salary:", access_employee_salary(employee_dict, employee_to_check))
