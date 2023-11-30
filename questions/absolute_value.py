# 7. Write a program to find out the absolute value of a number n

def absolute_value(n):
    if n < 0:
        abs_value = -n
    else:
        abs_value = n
    return abs_value


data = int(input("Enter Number: "))
result = absolute_value(data)
print("Absolute Value: ", result)

# ------------------------------------------------------------------


def absolute_value(n):
    value = abs(n)
    return value


data = int(input("Enter Number: "))
result = absolute_value(data)
print("Absolute Value: ", result)
