# Требуется выполнить сортировку временных моментов, заданных в часах, минутах и секундах.
#
# Во входном файле INPUT.TXT в первой строке записано число N (1 ≤ N ≤ 100), а в последующих N строках
# N моментов времени. Каждый момент времени задается 3 целыми числами - часы (от 0 до 23), минуты
# (от 0 до 59) и секунды (от 0 до 59).
#
# В выходной файл OUTPUT.TXT выведите моменты времени, упорядоченные в порядке неубывания без ведущих нулей.
# from datetime import time
#
# n = int(input())
# list_time = []
#
# for i in range(n):
#     hour, minute, second = map(int, input().split())
#     list_time.append(time(hour, minute, second))
#
# sort_list = sorted(list_time)
#
# for i in range(n):
#     formatted_time = sort_list[i].strftime("%H %M %S")
#     print(formatted_time)

n = int(input())
list_time = []

for i in range(n):
    hour, minute, second = map(int, input().split())
    x = 3600 * hour + 60 * minute + second
    list_time.append(x)

sort_list = sorted(list_time)

for i in range(n):
    hour = sort_list[i] // 3600
    minute = sort_list[i] // 60 % 60
    second = sort_list[i] % 60
    print(hour, minute,second)
