print('Курс Основы программирования начался') # №1


print(16823 * 12302 % 3092) # №2


age = 15 # №3
name = 'Владислав'
if (0 < age < 75) and (name != 'Иван'):
    if age >= 16:
        print('Поздравляем вы поступили в ВГУИТ')
    elif age < 16:
        print('Сначала нужно окончить школу!')
        print('Осталось учиться:', 16 - age, 'лет')


seconds = 18724981728947 # №4
print('дни:часы:минуты:секунды')
days = seconds // 86400
seconds %= 86400
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(days, ':', hours, ':', minutes, ':', seconds)


n = 65 # №5
print(n + (n ** 2) + (n ** 3) + (n ** 4) + (n ** 5))


x = 7 # №6
y = 8
print(x, y)
a = x
x = y
y = a
print(x, y)


number = 1284 # №7
if number % 2 == 0:
    print('Чётное')
else:
    print('Нечётное')