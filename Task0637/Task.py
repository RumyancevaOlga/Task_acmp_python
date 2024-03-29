# В полуфинале студенческого чемпионата мира по программированию NEERC (http://neerc.ifmo.ru)
# участвуют команды из n институтов. Участники для проведения соревнований распределяются по k залам,
# по правилам соревнований в одном зале может находиться не более одной команды от института.
#
# Многие институты уже подали заявки на участие в полуфинале. Оргкомитет полуфинала хочет допустить
# до участия максимально возможное количество команд. При этом, разумеется, должна существовать возможность
# рассадить их по залам без нарушения правил.
#
# Напишите программу, определяющую максимальное количество команд, которые можно допустить до участия в полуфинале.

n = int(input())
a_i = list(map(int, input().split()))
k = int(input())
count = 0
for i in range(n):
    if a_i[i] < k:
        count += a_i[i]
    else:
        count += k
print(count)
