def count_frequency_tuple(input_tuple):
    frequency_dict = {}

    for element in input_tuple:
        if element in frequency_dict:
            frequency_dict[element] += 1
        else:
            frequency_dict[element] = 1

    return frequency_dict


my_tuple = (1, 2, 3, 4, 1, 2, 3, 1, 2, 1)
result = count_frequency_tuple(my_tuple)

print("Element frequencies:")
for element, frequency in result.items():
    print(f"{element}: {frequency} times")
