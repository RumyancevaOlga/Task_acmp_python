# Будильник
# (Время: 1 сек. Память: 16 Мб Сложность: 12%)
# Известный исследователь Чарльз Ф. Мантц, устав от долгого путешествия через 
# джунгли, лег спать в 10 часов вечера, но предварительно он завел будильник на 
# 12 часов следующего дня. Но проспать 14 часов ему не удалось – будильник 
# зазвонил через 2 часа. Исследователь забыл, что на будильнике, имеющем 
# 12-тичасовой циферблат, можно задать время до звонка только менее 12 часов.

# Напишите программу, которая определяет, сколько часов успеет проспать 
# исследователь, прежде чем будильник его разбудит.

# Входные данные
# В единственной строке входного файла INPUT.TXT записаны два целых числа S и T 
# (1 ≤ S, T ≤ 12; S ≠ T), разделенные одним пробелом - час, когда исследователь 
# лег спать, и час, на который он установил будильник.

# Выходные данные
# В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое 
# число – через сколько часов зазвонит будильник.

with open('INPUT.txt', 'r') as my_f:
    S, T = map((int), my_f.readline().split())

if S > T :
    sleep_hours = 12 - S + T
else:
    sleep_hours = T - S

with open('OUTPUT.txt', 'w') as my_f1:
    my_f1.write(str(sleep_hours))