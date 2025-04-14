# Лиса Алиса и кот Базилио вырастили денежное дерево. И выросли на нем трехрублевые и
#  пятирублевые золотые монеты. Лиса Алиса себе взяла трехрублевые монеты, а коту Базилио
# отдала пятирублевые монеты. Посетовав на свою скромность, она предложила впредь рассчитываться
# за покупки вместе, деньги давать без сдачи и минимальным числом монет. Известно, что они сделали
# покупку стоимостью N рублей, при этом они рассчитались без сдачи.
#
# Вам следует написать программу, которая определяет: сколько монет внес кот Базилио,
# и сколько монет внесла лиса Алиса.

n = int(input())
basilio = 5
alisa = 3
count_b = 0
count_a = 0

if n % basilio == 0:
    count_b = n // basilio
elif n % basilio == 1 or n % basilio == 4:
    count_b = (n - basilio) // basilio
    count_a = ((n % basilio) + basilio) // alisa
elif n % basilio == 2:
    count_b = (n - (2 * basilio)) // basilio
    count_a = ((n % basilio) + (2 * basilio)) // alisa
elif n % basilio == 3:
    count_b = n // basilio
    count_a = (n % basilio) // alisa

print(count_b, count_a)
