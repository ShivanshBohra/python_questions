# 9. Write a program to find out divisibility of a number n by another number
# m, where m and n are integers input by the user


def divisibility_rule(n, divisor):
    """"Return True if n is divisible by n, Otherwise False"""
    return n % divisor == 0


print(divisibility_rule(5, 2))
print(divisibility_rule(10, 3))
print(divisibility_rule(6, 2))
