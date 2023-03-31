# Четырехзначный палиндром
# (Время: 1 сек. Память: 16 Мб Сложность: 10%)
# Требуется написать программу, определяющую, является ли четырехзначное 
# натуральное число N палиндромом, т.е. числом, которое одинаково читается 
# слева направо и справа налево.

# Входные данные
# Входной файл INPUT.TXT содержит натуральное число N (1000 ≤ N ≤ 9999).

# Выходные данные
# В выходной файл OUTPUT.TXT следует вывести слово «YES», если число N 
# является палиндромом, или «NO» – если нет.

with open('INPUT.txt', 'r') as my_f:
    number = int(my_f.readline())

reverseNumber = number % 10
numberNew = number // 10

for i in range (0, 3):
    reverseNumber = reverseNumber * 10 + numberNew % 10
    numberNew = numberNew // 10

if number == reverseNumber: result = 'YES'
else: result = 'NO'

with open('OUTPUT.txt', 'w') as my_f1:
    my_f1.write(result)