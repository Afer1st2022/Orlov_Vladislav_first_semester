def F():    
    A = []
    a = int(input('Введите размер квадратной матрицы: '))
    for i in range(a):
        A.append([])
    for i in range(a):
        for j in range(a):
            A[i].append(0)
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][i] = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if j > i:
                A[i][j] = int(input('Введите число: '))
    for i in range(len(A)):
        for j in range(len(A[i])):
            if j < i:
                A[i][j] = A[j][i]
    for i in range(len(A)):
        print(A[i])


F()


def H():
    A = []
    a = int(input('Введите размер квадратной матрицы: '))
    for i in range(a):
        A.append([])
        for j in range(a):
            A[i].append(int(input('Введите число: ')))
    print('Массив до: ')
    for i in range(len(A)):
        print(A[i])
    B = []
    for i in range(len(A)):
            B.append(A[i][i])
    print()
    print(B, 'Массив значений по диагонали')
    b = sum(B)
    print()
    print(b, 'След матрицы')
    print()
    for i in range(len(A)):
        for j in range(len(A[i])):
            if (i + 1) % 2 == 0:
                A[i][j] /= b
    print('Массив после: ')
    for i in range(len(A)):
        print(A[i])


H()