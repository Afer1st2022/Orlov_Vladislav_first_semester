# №1
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
d = a + b + c
print(d)

# №2
a = int(input('Введите длину первого катета: '))
b = int(input('Введите длину второго катета: '))
S = (1 / 2) * a * b
print('Площадь треугольника равна: ', S)

# №3
n = int(input('Введите количество минут: '))
if n < 0:
    print('Неверное количество минут')
elif n < 1440:
    hours = n // 60
    minutes = n % 60
    print('Часов: ', hours, ' Минут: ', minutes)
elif n % 1440 == 0 or n == 1440:
    print('00:00')
elif n > 1440:
    while n > 1440:
        n = n - 1440
    hours = n // 60
    minutes = n % 60
    print('Часов: ', hours, ' Минут: ', minutes)
    
