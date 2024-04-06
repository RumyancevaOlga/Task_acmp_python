# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.
n = int(input())
if n > 0:
    result = sum(range(1, n + 1))
elif n < 0:
    result = sum(range(n, 2))
else:
    result = 1
print(result)
