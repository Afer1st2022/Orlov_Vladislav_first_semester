# №1
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
d = a + b + c
print(d)
print()


# №2
a = int(input('Введите длину первого катета: '))
b = int(input('Введите длину второго катета: '))
S = (1 / 2) * a * b
print('Площадь треугольника равна: ', S)
print()


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
print()


# №4
def F(n):
    a = int(input('Введите расстояние между рядами: '))
    b = int(input('Введите расстояние между дырочками в ряду: '))
    l = int(input('Введите длину свободного конца шнурка: '))
    N = int(input('Введите количество дырочек в каждом ряду: '))
    S = 2 * l + (2 * N - 1) * a + (2 * N - 2) * b
    return(S)


print(F(n))
print()


# №5
def F(n):
    n1 = int(input('Введите первое число: '))
    n2 = int(input('Введите второе число: '))
    n3 = int(input('Введите третье число: '))
    return min(n1, n2, n3)


print(F(n))
print()


# №6
def F(n):
    A1 = int(input('Введите номер столбца первой клетки: '))
    A2 = int(input('Введите номер строки первой клетки: '))
    B1 = int(input('Введите номер столбца второй клетки: '))
    B2 = int(input('Введите номер строки второй клетки: '))
    A = A1 + A2
    B = B1 + B2
    A_is_black = False
    B_is_black = False
    if A % 2 == 0:
        A_is_black = True
    if B % 2 == 0:
        B_is_black = True
    if (A_is_black and B_is_black) or (not(A_is_black) and not(B_is_black)):
        return 'Да'
    else:
        return 'Нет'


print(F(n))
print()


# №7
def F(n):
    year = int(input('Введите год: '))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 'Да'
    else:
        return 'Нет'


print(F(n))
print()


# №8
def F(n):
    ch1 = int(input('Введите первое число: '))
    ch2 = int(input('Введите второе число: '))
    ch3 = int(input('Введите третье число: '))
    if ch1 == ch2 == ch3:
        return 3
    elif ch1 == ch2 or ch1 == ch3 or ch2 == ch3:
        return 2
    else:
        return 0


print(F(n))
print()


# №9
def F():
    n = int(input('Введите количество плиток по горизонтали: '))
    m = int(input('Введите количество плиток по вертикали: '))
    k = int(input('Введите желаемое количество долей: '))
    if k % n == 0 or k % m == 0:
        return 'Да'
    else:
        return 'Нет'


print(F())
print()