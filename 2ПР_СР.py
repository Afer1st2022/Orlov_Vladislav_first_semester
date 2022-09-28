# 7 Вариант
import math
x = float(input('Введите значение x: '))
y = float(input('Введите значение y: '))
z = float(input('Введите значение z: '))
s = (5 * math.atan(x)) - ((math.acos(x) * (x + (3 * abs(x - y)) + (x ** 2))) / (4 * (z * (abs(x - y)) + (x ** 2))))
print('s = {0:.3f}'.format(s))