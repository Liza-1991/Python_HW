import math


def square(side):
    s = side ** 2
    return s


x = float(input())
result = square(x)
rounded = math.ceil(result)
print(rounded)
