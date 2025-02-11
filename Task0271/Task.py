# Числа Фибоначчи строятся следующим образом: 1, 1, 2, 3, 5, …. В этой последовательности,
# начиная с третьего числа, каждый следующий член равен сумме двух предыдущих. Получаем, что,
# например, шестое число равно 8, а десятое - 55.
#
# Требуется написать программу, которая определяет, является ли заданное число числом Фибоначчи.

num = int(input())

f1 = 1
f2 = 1
count = 2

while num >= f2:
    if num == f2:
        print(1)
        print(count)
        exit()
    else:
        temp = f2
        f2 = f1 + f2
        f1 = temp
        count += 1
else:
    print(0)
