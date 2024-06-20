"""Заполнение змейкой
Даны числа n и m. Создайте массив A[n][m] и заполните его змейкой (см. пример).

Входные данные
Программа получает на вход два числа n и m.

Выходные данные
Программа должна вывести  полученный массив, при этом между числами может быть любое количество пробелов.

Sample Input 1:

4 10
Sample Output 1:

0  1  2  3  4  5  6  7  8  9
19 18 17 16 15 14 13 12 11 10
20 21 22 23 24 25 26 27 28 29
39 38 37 36 35 34 33 32 31 30

"""
n, m = map(int, input().split())
a = []
for i in range(n):
    b = []
    for j in range(m):
        b.append(0)
    a.append(b)
index = 0
for r in range(n):
    if r % 2 == 0:
        for c in range(m):
            a[r][c] = index
            index +=1
    else:
        for c in range(m-1, -1, -1):
            a[r][c] = index
            index += 1


for i in range(n):
    for j in range(m):
        print(str(a[i][j]).ljust(1), end=" ")
    print()