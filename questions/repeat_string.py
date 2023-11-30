# 4. Write a program to repeat the string ‘‘GOOD MORNING” n times. Here ‘n’
# is an integer entered by the user

def repeat_string(s, n):
    i = 0
    print("Values are: ")
    while i < n:
        print(" ", s)
        i += 1


result = input("Enter a String: ")
times = int(input("How many times it will repeat: "))
repeat_string(result, times)
