"""Дана прямоугольная матрица размером NxM, в которой заполнены значения только в первом столбце и в первом ряду. Все остальные элементы равны нулю и мы считаем их незаполненными.

Ваша задача заполнить каждый пустой элемент путем сложения соседа слева и соседа сверху. Начинать нужно с тех элементов, у которых оба указанных соседа заполнены (не равны нулю)

Входные данные
Программа сперва принимает в одной строке на вход два числа N и M - количество строк и столбцов в списке, а затем в N строках записаны элементы списка.

Выходные данные
Вывести заполненную матрицу

Sample Input 1:

5 4
1 1 1 1
1 0 0 0
1 0 0 0
1 0 0 0
1 0 0 0
Sample Output 1:

1 1 1 1
1 2 3 4
1 3 6 10
1 4 10 20
1 5 15 35
"""
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
    
for row in range(1, n):
    for column in range(1, m):
         a[row][column] = a[row-1][column]+a[row][column-1]
            
        
    
for row in range(n):
    for column in range(m):
        print(a[row][column], end=" ")
    print()