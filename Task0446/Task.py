# На хоккейном стадионе в одном большом городе расположено большое прямоугольное табло.
# Оно имеет n строк и m столбцов (то есть состоит из n x m ячеек).
# Во время хоккейного матча это табло служит для отображения счета и времени,
# прошедшего с начала тайма, а в перерывах на нем показывают различную рекламу.
#
# В связи с этим возникла задача проверки возможности показа на этом табло
# определенной рекламной заставки. Заставка также, как и табло, имеет размер n строк на m столбцов.
# Каждая из ячеек заставки окрашена в один из четырех цветов - трех основных:
# красный - R, зеленый - G, синий - B и черный - .(точка).
#
# Каждая из ячеек табло характеризуется своими цветопередаточными возможностями.
# Любая из ячеек табло может отображать черный цвет - это соответствует тому,
# что на нее вообще не подается напряжение. Также каждая из ячеек может отображать
# некоторое подмножество множества основных цветов. В этой задаче эти подмножества
# будут кодироваться следующим образом:
#
# 0 - ячейка может отображать только черный цвет;
# 1 - ячейка может отображать только черный и синий цвета;
# 2 - ячейка может отображать только черный и зеленый цвета;
# 3 - ячейка может отображать только черный, зеленый и синий цвета;
# 4 - ячейка может отображать только черный и красный цвета;
# 5 - ячейка может отображать только черный, красный и синий цвета;
# 6 - ячейка может отображать только черный, красный и зеленый цвета;
# 7 - ячейка может отображать только черный, красный, зеленый и синий цвета.
# Напишите программу, которая по описанию табло и заставки определяет:
# возможно ли на табло отобразить эту заставку.


n, m = map(int, input().split())

code = {'.': 0, 'B': 1, 'G': 2, 'R': 4}

list_tab = []
for i in range(n):
    list_tab.append(input())

list_code = []
for i in range(n):
    list_code.append(input().split())
    for j in range(m):
        k = int(list_code[i][j])
        if list_tab[i][j] != '.' and (code[list_tab[i][j]] & k == 0):
            print('NO')
            exit()

print('YES')
