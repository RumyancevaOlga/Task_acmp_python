# Баскетбол
# (Время: 1 сек. Память: 16 Мб Сложность: 5%)
# Известны результаты каждой из 4х четвертей баскетбольной встречи. Нужно определить победителя матча. Побеждает 
# команда, набравшая больше очков в течение всего матча.

# Входные данные
# Входной файл INPUT.TXT содержит 4 строки, в каждой строке находится два целых числа a и b – итоговый счет в 
# соответствующей четверти. а – количество набранных очков за четверть первой командой, b – количество очков, 
# набранных за четверть второй командой. (0 ≤ a,b ≤ 100).

# Выходные данные
# В выходной файл OUTPUT.TXT выведите номер выигравшей команды, в случае ничьей следует вывести «DRAW».

with open('INPUT.txt', 'r') as my_f:
    all_points = my_f.readlines()

first_quarter = all_points[0].strip().split()
second_quarter = all_points[1].strip().split()
third_quarter = all_points[2].strip().split()
fourth_quarter = all_points[3].strip().split()

first_team_points = int(first_quarter[0]) + int(second_quarter[0]) + int(third_quarter[0]) + int(fourth_quarter[0])
second_team_points = int(first_quarter[1]) + int(second_quarter[1]) + int(third_quarter[1]) + int(fourth_quarter[1])

winner = '1'

if second_team_points > first_team_points:
    winner = '2'
elif second_team_points == first_team_points:
    winner = 'DRAW'

with open('OUTPUT.txt', 'w') as my_f1:
    my_f1.write(winner)
