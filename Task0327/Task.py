# Вова купил билет в трамвае 13-го маршрута и сразу посчитал суммы первых трёх цифр и последних
# трёх цифр номера билета (номер у билета шестизначный). Оказалось, что суммы отличаются ровно
# на единицу. «Я в одном шаге от счастья», — подумал Вова, — «или предыдущий или следующий билет
# точно счастливый». Прав ли он?

k = int(input())
for i in range(k):
    ticket = int(input())
    previous = ticket - 1
    next_ = ticket + 1
    a_p, b_p, a_n, b_n = 0, 0, 0, 0
    for j in range(3):
        a_p += previous % 10
        a_n += next_ % 10
        previous //= 10
        next_ //= 10
    for j in range(3):
        b_p += previous % 10
        b_n += next_ % 10
        previous //= 10
        next_ //= 10
    if a_p == b_p or a_n == b_n:
        print('Yes')
    else:
        print('No')
