#1
def F1():
    N = int(input('Введите число N: '))
    A = []
    for i in range(1, N):
        a = i ** 2
        if a <= N:
            A.append(a)
        else:
            break
    print(A)
F1()


#2
def F2():
    a = int(input('Введите число не меншьее 2: '))
    is_end = False
    for i in range(2, a):
        if not is_end:
            if a % i == 0:
                print(i)
                is_end = True
        else:
            break
F2()


#3
def F3():
    N = int(input('Введите число N: '))
    is_end = False
    count = 1
    a = 2
    if 1 <= N <= 3:
        is_end = True
        print(count)
    while not is_end:
        count += 1
        a *= 2
        if N < a:
            print(count - 1)
            is_end = True
            break
F3()


#4
def F4():
    x = int(input('Введите число x: '))
    y = int(input('Введите число y: '))
    count = 1
    is_end = False
    while not is_end:
        count += 1
        x *= 1.1
        if x >= y:
            is_end = True
            print(count)
            break
F4()


#5
def F5():
    is_end = False
    A = []
    while not is_end:
        a = int(input('Введите новое неотрицательное число. Чтобы завершить введите "0": '))
        if a != 0:
            A.append(a)
        else:
            is_end = True
            print(len(A))
            break
F5()


#6
def F6():
    is_end = False
    A = []
    while not is_end:
        a = int(input('Введите новое неотрицательное число. Чтобы завершить введите "0": '))
        if a != 0:
            A.append(a)
        else:
            is_end = True
            print(sum(A) / len(A))
            break
F6()


#7
def F7():
    is_end = False
    count = 0
    A = []
    while not is_end:
        a = int(input('Введите новое неотрицательное число. Чтобы завершить введите "0": '))
        if a != 0:
            A.append(a)
        else:
            break
    for i in range(len(A) - 1):
        if A[i + 1] > A[i]:
            count += 1
    print(count)
F7()


#8
def F8():
    is_end = False
    A = []
    count = 1
    max_count = 0
    while not is_end:
        a = int(input('Введите новое неотрицательное число. Чтобы завершить введите "0": '))
        if a != 0:
            A.append(a)
        else:
            is_end = True
            break
    for i in range(len(A) - 1):
        if A[i] == A[i + 1]:
            count += 1
        elif count > max_count:
            max_count = count
            count = 1
        else: count = 1
    if count > max_count:
        max_count = count
    print(max_count)
F8()