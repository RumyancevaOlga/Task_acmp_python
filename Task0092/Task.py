# Журавлики
# (Время: 1 сек. Память: 16 Мб Сложность: 7%)
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый 
# ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза 
# больше журавликов, чем Петя и Сережа вместе?

# Входные данные
# В единственной строке входного файла INPUT.TXT записано одно натуральное число S – общее количество сделанных 
# журавликов (S < 106).

# Выходные данные
# В единственную строку выходного файла OUTPUT.TXT нужно вывести три числа, разделенных пробелами – количество 
# журавликов, которые сделал каждый ребенок (Петя, Катя и Сережа).

with open('INPUT.txt', 'r') as my_f:
    all_cranes = my_f.readline()

peter_and_sergio = int(all_cranes) / 6
peter_and_sergio = int(peter_and_sergio)

kate = peter_and_sergio * 4

with open('OUTPUT.txt', 'w') as my_f1:
    my_f1.write(f'{str(peter_and_sergio)} {str(kate)} {str(peter_and_sergio)}')
