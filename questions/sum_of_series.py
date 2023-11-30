# 13.Write a program to find the sum of 1+ 1/8 + 1/27......1/n3, where n is the
# number input by the user. (Summation of a series)


def series_sum(n):
    result = 0

    for i in range(1, n+1):
        result = result + 1 / i ** 3
    return result


result1 = series_sum(2)
print(result1)
