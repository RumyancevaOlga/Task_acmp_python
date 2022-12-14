# Три толстяка
# (Время: 1 сек. Память: 16 Мб Сложность: 7%)
# Три толстяка решили поспорить: кто из них самый тяжелый. После взвешивания оказалось, что их масса соответственно 
# M1, M2 и M3 килограмм. Считается, что масса толстяка должна быть не менее 94 и не более 727 килограмм.

# Помогите определить массу самого тяжелого из них, либо выяснить, что была допущена ошибка при взвешивании.

# Входные данные
# Входной файл INPUT.TXT содержит три целых числа M1, M2 и M3, разделенные пробелом. Все числа целые и не превосходят 
# 10 000 по абсолютной величине.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите массу самого тяжелого толстяка в случае корректного взвешивания, либо слово 
# «Error» в противном случае.

with open('INPUT.txt', 'r') as my_f:
    mass = my_f.readline().split()

if 727 >= int(mass[0]) >= 94 and 727 >= int(mass[1]) >= 94 and 727 >= int(mass[2]) >= 94:
    m1 = int(mass[0])
    m2 = int(mass[1])
    m3 = int(mass[2])
    max = m1
    if m2 > max:
        max = m2
    if m3 > max:
        max = m3
    max = str(max)
else:
    max = 'Error'

with open('OUTPUT.txt', 'w') as my_f1:
    my_f1.write(max)




