# Длина отрезка
# (Время: 1 сек. Память: 16 Мб Сложность: 12%)
# Отрезок, заданный координатами своих концевых точек
# Отрезок задан координатами своих концевых точек. Требуется вычислить 
# длину этого отрезка.

# Входные данные
# Первая строка входного файла INPUT.TXT содержит координаты концов 
# отрезка в формате X1 Y1 X2 Y2 . Все координаты – целые числа, не 
# превышающие 1000 по абсолютной величине.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите длину отрезка с точностью 10-5.

with open('INPUT.txt', 'r') as my_f:
    X1, Y1, X2, Y2 = map((int), my_f.readline().split())

length = round((((X2 - X1) * (X2 - X1) + (Y2 - Y1) * (Y2 - Y1)) ** 0.5), 5)

with open('OUTPUT.txt', 'w') as my_f1:
    my_f1.write(str(length) + "\n")