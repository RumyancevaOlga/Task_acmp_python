# Выведите в выходной файл округленное до n знаков после десятичной точки число E.
# В данной задаче будем считать, что число Е в точности равно 2.7182818284590452353602875.

e = '2.7182818284590452353602875'

n = int(input())
result = '2.'

if n == 0:
    print(3)
else:
    for i in range(n - 1):
        result += e[i + 2]
    if n == 25:
        result += e[26]
    elif int(e[n + 2]) < 5:
        result += e[n + 1]
    elif int(e[n + 2]) >= 5:
        result += str(int(e[n + 1]) + 1)
    print(result)
