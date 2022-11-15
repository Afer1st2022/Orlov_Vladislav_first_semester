def F():
    file = open('C:\\Users\\Afer1st\\Desktop\\Орлов Владислав Максимович_У-223_vvod.txt', 'r')
    file2 = open('C:\\Users\\Afer1st\\Desktop\\Орлов Владислав Максимович_У-223_vivod.txt', 'w')
    A = []
    a = int(file.readline())
    C = list(map(int, file.readline().split()))
    a = int(a)
    for i in range(a):
        A.append([])
    for i in range(a):
        for j in range(a):
            A[i].append(0)
    for i in range(len(A)):
        for j in range(len(A[i])):
            A[i][i] = 0
    count = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if j > i:
                count += 1
                A[i][j] = C[count - 1]
    for i in range(len(A)):
        for j in range(len(A[i])):
            if j < i:
                A[i][j] = A[j][i]
    for i in range(len(A)):
        file2.write(str(A[i]) + '\n')
        


F()


def H():
    A = []
    file = open('C:\\Users\\Afer1st\\Desktop\\Орлов Владислав Максимович_У-223_vvod2.txt', 'r')
    file2 = open('C:\\Users\\Afer1st\\Desktop\\Орлов Владислав Максимович_У-223_vivod2.txt', 'w')
    a = int(file.readline())
    b = []
    for i in range(a):
        b += list(map(int, file.readline().split()))
    count = 0
    for i in range(a):
        A.append([])
        for j in range(a):
            count += 1
            A[i].append(b[count - 1])
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
    for i in range(len(A)):
        file2.write(str(A[i]) + '\n')    


H()