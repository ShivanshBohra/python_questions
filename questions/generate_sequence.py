# 10.Write a program to generate the sequence: –5, 10, –15, 20, –25….. upto
# n, where n is an integer input by the user

def sequence_generate(n):
    sequence = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            sequence.append(5 * i)
        else:
            sequence.append(-5 * i)
    return sequence


n = int(input("Enter the value of n: "))

result = sequence_generate(n)
print("Generated Sequence:", result)
