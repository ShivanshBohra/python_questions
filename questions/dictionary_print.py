# 34. Write a Python code to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are the square of the
# keys.


def dictionary_print():
    d = dict()
    for i in range(1, 16):
        d[i] = i * i
    return d


print(dictionary_print())
