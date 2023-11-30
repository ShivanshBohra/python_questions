# 3. Write a program to swap two numbers i. using a third variable ii. Without
# using a third variable


# without using a third variable
def swap_numbers(x, y):
    x = x + y
    y = x - y
    x = x - y
    return x, y


input1 = int(input("Enter value of x: "))
input2 = int(input("Enter value of y: "))

result1, result2 = swap_numbers(input1, input2)
print("x:", result1)
print("y:", result2)


# using a third variable
def swap_numbers(x, y):
    temp = x
    x = y
    y = temp
    return x, y


input1 = int(input("Enter value of x: "))
input2 = int(input("Enter value of y: "))

result1, result2 = swap_numbers(input1, input2)
print("x:", result1)
print("y:", result2)
