# Пусть задан массив целых чисел а1, а2, ..., аn. Назовем его подмассивом f(i,j) массив, составленный из чисел массива аi, ai+1,..., aj-1, aj.
# Напишите программу, которая будет выводить подмассивы массива a.

n = int(input())
a = list(map(int, input(). split()))
m = int(input())
for b in range(m):
    i, j = map(int, input().split())
    for c in range(i - 1, j):
        print(a[c], end=' ')
