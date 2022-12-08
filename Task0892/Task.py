# Время года
# (Время: 1 сек. Память: 16 Мб Сложность: 10%)
# По заданному номеру месяца в году требуется определить время года.

# Входные данные
# Входной файл INPUT.TXT содержит натуральное число N (N≤100) – номер месяца.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите для летних месяцев значение «Summer», для 
# зимних – «Winter», для весенних – «Spring», для осенних – «Autumn». Если число 
# не соответствует возможному значению месяца, то в этом случае следует вывести 
# «Error».

with open ("INPUT.txt", "r") as my_f:
    month = int(my_f.readline())

if 2 < month < 6 :
    result = "Spring"
elif 5 < month < 9 :
    result = "Summer"
elif 8 < month < 12 :
    result = "Autumn"
elif 0 < month < 3 or month == 12:
    result = "Winter"
else:
    result = "Error"

with open ("OUTPUT.txt", "w") as my_f2:
    my_f2.write(result)

