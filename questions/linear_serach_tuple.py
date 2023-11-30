# 23. Write a program to implement linear search on tuple of numbers

pos = -1


def linear_search_tuple(input_tuple, target):
    i = 0

    while i < len(input_tuple):
        if input_tuple[i] == target:
            globals()['pos'] = i
            return True
        i = i + 1
    return False


my_tuple = (3, 5, 6, 7, 8)
target_number = 7

if linear_search_tuple(my_tuple, target_number):
    print(f"Found {target_number} at index {pos}")
else:
    print(f"{target_number} Not Found")
