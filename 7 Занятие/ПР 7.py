import ast


def F():
    A = [1, 54, 5, 66, 76, 35, 89, 215, 67]
    B = 0
    for i in range(0, len(A), 2):
        B += A[i]
    print(B)
    C = 1
    for i in range(1, len(A), 2):
        C *= A[i]
    print(C)
F()


def F2():
    global max, min
    A = [1, 54, 5, 66, 76, 35, 89, 215, 67]
    max = A.index(max(A))
    min = A.index(min(A))
    b = A[min]
    A[min] = A[max]
    A[max] = b
    print(A)
F2()