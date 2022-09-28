x1 = int(input('Введите первое целое число: '))
x2 = int(input('Введите второе целое число: '))
x3 = int(input('Введите третье целое число: '))


def F(n):
    if 1 <= n <= 3:
        return n


print(F(x1))
print(F(x2))
print(F(x3))