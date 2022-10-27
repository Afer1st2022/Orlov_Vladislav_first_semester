#1
def F(A, B):
  for i in range(A, B + 1):
      print(i)
A = int(input('Введите число A, так чтобы A <= B: '))
B = int(input('Введите число B, так чтобы A <= B: '))
F(A, B)


#2
X = int(input('Введите число A: '))
Z = int(input('Введите число B: '))
def C(X, Z):
  if X < Z:
      for i in range(X, Z + 1):
          print(i)
  elif X > Z:
      for i in reversed(range(Z, X + 1)):
          print(i)
C(X, Z)


#3
X = int(input('Введите число A, так чтобы A > B: '))
Z = int(input('Введите число B, так чтобы A > B: '))
def D(X, Z):
  if Z % 2 != 0:
      for i in reversed(range(Z, X + 1, 2)):
          print(i)
  else:
      for i in reversed(range(Z + 1, X + 1, 2)):
          print(i)
D(X, Z)


#4
def B():
  N = int(input('Введите количество чисел: '))
  A = []
  for i in range(N):
      A.append(int(input('Введите новое число: ')))
  print(sum(A))
B()


#5
def H():
  n = int(input('Введите число n: '))
  a = 0
  for i in range(1, n + 1):
      a += i**3
  print(a)
H()


#6
def J():
   n = int(input('Введите натуральное число n: '))
   a = 1
   for i in range(1, n + 1):
      a *= i
   print(a)
J()


#7
def I():
   a = 1
   b = 1
   i = 1
   n = int(input('Введите натуральное число n: '))
   while i != n:
       i += 1
       a *= i
       b += a
   print(b)
I()


#8
def K():
   n = int(input('Введите число n, так чтобы n <= 9: '))
   for i in range(1, n + 1):
       a = ''
       for j in range(1, i + 1):
           a += str(j)
       print(a)
K()


#9
def Fib(k):
   if k == 1 or k == 2:
       return 1
   return Fib(k - 1) + Fib(k - 2)

def L():
   N = int(input('Введите число N: '))
   A = []
   i = 1
   while i != N + 1:
       A.append(Fib(i))
       i += 1
   print(sum(A))
L()


#10
def Fib(k):
   if k == 1 or k == 2:
       return 1
   return Fib(k - 1) + Fib(k - 2)

def FIB():
   N = int(input('Введите число N: '))
   K = int(input('Введите число K: '))
   A = []
   for i in range(N):
       A.append(Fib(K))
       K += 1
   print(sum(A))
FIB()
