from functools import reduce
num = [1, 2, 3, 4, 5, 6, 7]
print(reduce(lambda x, y: x+y, num))

num = [1, 2, 3, 4, 5,-10, -4]
num1 = reduce(lambda x, y: x*y, num)
print(num1)
print(type(num1))

num = [1, 2, 3, 4, 5,-10, -4]
num2 = map(lambda x: x + 10, num)
print(list(num2))
print(type(num2))

num = [1, 2, 3, 4, 5,-10, -4]
num3 = filter(lambda x: x+4, num)
print(list(num3))
print(type(num3))