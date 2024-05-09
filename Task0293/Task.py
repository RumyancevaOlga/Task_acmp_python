# В некотором государстве действует N фирм, конкурирующих между собой. У каждой фирмы есть некоторая
# прибыль в год, равная V[i] американских рублей. У царя есть любимые фирмы, а есть нелюбимые.
# Соответственно, налог для всех фирм разный и назначается царем в индивидуальном порядке.
# Налог на i-ую фирму равен p[i] процентов.
#
# Собиратели статистики решили посчитать, с какой фирмы в государственную казну идет наибольший доход
# (в казну идут все налоги). К сожалению, они не учили в детстве ни математику, ни информатику
# (так что учитесь, дети!), и их задача резко осложняется.
#
# Помогите им в этой нелегкой задаче.

n = int(input())
list_ = list(map(int, input().split()))
list_proc = list(map(int, input().split()))
result = 0
count = 0
for i in range(n):
    deposit = list_[i] * (list_proc[i] / 100)
    if result < deposit:
        result = deposit
        count = i + 1
if count == 0:
    count = 1
print(count)