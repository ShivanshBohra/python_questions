# 37. Write a code in python to print the Fibanocci sequence upto n terms, n is
# entered by the user.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


nterms = int(input("How many terms you want to print: "))
for i in range(nterms):
    print(fibonacci(i))
