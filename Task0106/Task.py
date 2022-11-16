# Монетки
# (Время: 1 сек. Память: 16 Мб Сложность: 8%)
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число 
# монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Входные данные
# В первой строке входного файла INPUT.TXT записано натуральное число N (1 ≤ N ≤ 100) – число монеток. В каждой из 
# последующих N строк содержится одно целое число – 1 если монетка лежит решкой вверх и 0 если вверх гербом.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите минимальное количество монет, которые нужно перевернуть.

with open('INPUT.txt', 'r') as my_f:
    num = my_f.readlines()

numbers = []

for i in range(len(num)):
    numbers.append(int(num[i].strip()))

zero_count = 0
one_count = 0

for i in range(1, (len(num))):
    if numbers[i] == 0:
        zero_count += 1
    else:
        one_count += 1

if zero_count > one_count:
    result = one_count
else:
    result = zero_count

with open('OUTPUT.txt', 'w') as my_f1:
    my_f1.write(str(result))
