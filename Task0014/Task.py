# Требуется написать программу, определяющую наименьшее общее кратное (НОК) чисел a и b.

a, b = map(int, input().split())
a1, b1 = a, b
while a1 != 0 and b1 != 0:
    res = max(a1, b1) % min(a1, b1)
    a1, b1 = min(a1, b1), res
nod = max(a1, b1)
result = int((a * b) / nod)
print(result)
