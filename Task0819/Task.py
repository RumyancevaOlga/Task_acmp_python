# Прямоугольный параллелепипед
# (Время: 1 сек. Память: 16 Мб Сложность: 10%)
# Прямоугольный параллелепипед
# Прямоугольный параллелепипед - это объемная фигура, у которой шесть граней, 
# и каждая из них является прямоугольником. Моделями прямоугольного 
# параллелепипеда служат классная комната, кирпич, спичечная коробка. Длины трех 
# ребер прямоугольного параллелепипеда, имеющих общий конец, называют его 
# измерениями. На приведенном рисунке измерения представлены ребрами AB, BC и BF 
# с общим концом в точке B, а значения измерений равны их длинам a, b и c 
# соответственно.

# По заданным измерениям прямоугольного параллелепипеда Вам необходимо определить 
# площадь его поверхности и объем.

# Входные данные
# Единственная строка входного файла INPUT.TXT содержит разделенные пробелом три 
# натуральных числа a, b и c – измерения параллелепипеда, каждое из измерений не 
# превышает 106.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите через пробел два целых числа: площадь 
# поверхности и объем заданного параллелепипеда.

with open('INPUT.txt', 'r') as my_f:
    edges = my_f.readline().split()

a = int(edges[0])
b = int(edges[1])
c = int(edges[2])

S = 2*(a*c + c*b + a*b)
V = a*b*c

with open('OUTPUT.txt', 'w') as my_f1:
    my_f1.write(str(S) + ' ' + str(V))