# Необходимо представить целое число N в виде суммы M примерно равных целых чисел.
# Будем считать, что числа примерно равны, если они отличаются друг от друга не более чем на единицу.

n, m = map(int, input().split())

list_res = []

for i in range(m):
    list_res.append(n // m)

rod = n % m
i = m - 1

while rod > 0:
    list_res[i] += 1
    i -= 1
    rod -= 1

for i in range(m):
    print(list_res[i], end=' ')
