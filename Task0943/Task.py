# Напишите программу, которая выводит элемент из строки Y и столбца X матрицы размера N×M,
# которая заполнена следующим образом:

n, m, y, x = map(int, input().split())
matrix = []
in_matrix = []
for i in range(n):
    for j in range(m):
        in_matrix.append(j + i * m)
    if i % 2 == 1:
        in_matrix.reverse()
    matrix.append(in_matrix)
    in_matrix = []
print(matrix[y - 1][x - 1])
