# 33. Write 2 different python programs to reverse a string.

# Using a loop:

def reverse_string_loop(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str


original_string = "Hello, World!"
reversed_result = reverse_string_loop(original_string)
print(f"Original String: {original_string}")
print(f"Reversed String (using loop): {reversed_result}")


# Using string slicing:
def reverse_string_slicing(input_str):
    reversed_str = input_str[::-1]
    return reversed_str


# Example usage:
original_string = "Hello, World!"
reversed_result = reverse_string_slicing(original_string)
print(f"Original String: {original_string}")
print(f"Reversed String (using slicing): {reversed_result}")
