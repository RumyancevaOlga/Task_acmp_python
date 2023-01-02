# Спирт
# (Время: 1 сек. Память: 16 Мб Сложность: 10%)
# Каждому школьнику из курса органической химии известна формула молекулы 
# этилового спирта – C2H5(OH). Откуда видно, что молекула спирта состоит из двух 
# атомов углерода (C), шести атомов водорода (H) и одного атома кислорода (O).

# По заданному количеству атомов каждого из описанных выше элементов требуется 
# определить максимально возможное количество молекул спирта, которые могут 
# образоваться в процессе их соединения.

# Входные данные
# Первая строка входного файла INPUT.TXT содержит 3 натуральных числа: C, Н и O 
# – количество атомов углерода, водорода и кислорода соответственно. Все числа 
# разделены пробелом и не превосходят 1018.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите максимально возможное число молекул спирта, 
# которые могут получиться из атомов, представленных во входных данных.

with open('INPUT.txt', 'r') as my_f:
    numbers = my_f.readline().split()

C = int(numbers[0])
H = int(numbers[1])
O = int(numbers[2])

# count = 0

# while (C > 0 and H > 0 and O > 0):
#     C = C - 2
#     H = H - 6
#     O = O - 1
#     if (C >= 0 and H >= 0 and O >= 0): 
#         count += 1

C = C // 2
H = H // 6

if (C == 0 or H == 0 or O == 0): count = 0
else: count = min(C, H, O)

with open('OUTPUT.txt', 'w') as my_f2:
    my_f2.write(str(count))