# Ремонт
# (Время: 1 сек. Память: 16 Мб Сложность: 11%)
# Ваш любимый дядя – директор фирмы, которая делает евроремонты в офисах. 
# В связи с финансово-экономическим кризисом, дядюшка решил оптимизировать 
# свое предприятие.

# Давно ходят слухи, что бригадир в дядюшкиной фирме покупает лишнее количество 
# стройматериалов, а остатки использует для отделки своей новой дачи. Ваш дядя 
# заинтересовался, сколько в действительности банок краски необходимо для 
# покраски стен в офисе длиной L метров, шириной – W и высотой – H, если 
# одной банки хватает на 16м2, а размерами дверей и окон можно пренебречь? 
# Заказов много, поэтому дядя попросил написать программу, которая будет все 
# это считать.

# Входные данные
# Первая строка входного файла INPUT.TXT содержит три натуральных числа L, W, H 
# через пробел – длину, ширину и высоту офиса в метрах соответственно. Каждое из 
# них не превышает 1000.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите одно целое число – минимальное количество 
# банок краски, необходимых для покраски стен в офисе.

with open('INPUT.txt', 'r') as my_f:
    L, W, H = map((int), my_f.readline().split())

count_pots = ((L + W) * 2 * H  + 15) // 16

with open('OUTPUT.txt', 'w') as my_f1:
    my_f1.write(str(count_pots))