# 2. Write a python program to calculate area and perimeter of a rectangle

def calc_area_perimeter(l, b, w):
    area = l * b
    perimeter = (l + w) * 2
    return area, perimeter


result1, result2 = calc_area_perimeter(5, 7, 8)  # used positional argument
print("Area of a rectangle:", result1, "\nPerimeter of rectangle:", result2)
