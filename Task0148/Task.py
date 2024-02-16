# Даны два натуральных числа A и B. Требуется найти их наибольший общий делитель (НОД).

a, b = map(int, input().split())
while a != 0 and b != 0:
    res = max(a, b) % min(a, b)
    a, b = min(a, b), res
print(max(a,b))
