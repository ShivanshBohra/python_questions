# 25. Write a program to count the number of times a character appears in a
# given string using a dictionary

def count_characters(input_string):
    char_frequency = {}

    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    return char_frequency


input_string = "programming"
result = count_characters(input_string)

print("Character frequencies:")
for char, frequency in result.items():
    print(f"{char}: {frequency} times")
