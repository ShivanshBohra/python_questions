# 20. Write a program for counting the frequency of elements in a list

def count_frequency(arr):
    frequency_dict = {}

    for element in arr:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1

    return frequency_dict


my_list = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]
result = count_frequency(my_list)

print("Element frequencies:")
for element, frequency in result.items():
    print(f"{element}: {frequency} times")
