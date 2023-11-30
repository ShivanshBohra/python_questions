# 19. Write a program to implement linear search on list of numbers

pos = -1


def search(list, n):
    i = 0

    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1
    return False


list = [3, 5, 6, 7, 8]
n = 8
if search(list, n):
    print("Found", pos)
else:
    print("Not Found")
