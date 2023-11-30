# Q. 36 Write a python program to print the following pattern of numbers.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


def print_pattern():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


print_pattern()
