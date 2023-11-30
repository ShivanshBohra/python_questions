# 8. Write a program to sort 3 numbers

def sort_number(number):
    number_list = [int(digit) for digit in str(number)]
    asc_order = sorted(number_list)
    desc_order = sorted(number_list, reverse=True)
    return asc_order, desc_order


data = int(input("Enter numbers: "))
result = sort_number(data)
print("Ascending Order:", result[0])
print("Descending Order:", result[1])
