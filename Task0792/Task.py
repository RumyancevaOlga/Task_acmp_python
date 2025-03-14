# В стране Амбер очень сложные торгово-финансовые отношения. Если один торговец хочет обменять
# свой товар на товар другого торговца, тогда они идут в Торговую Гильдию Амбера. Наверное,
# вы подумали, что торговцы просто обменяются товарами и уйдут в разные стороны довольными от
# выгодной сделки? Как бы не так! Законы в Амбере таковы, что Торговая Гильдия может получить
# прибыль от сделки между двумя торговцами, равную нормирующему коэффициенту одного из торговцев,
# только в том случае, когда нормирующие коэффициенты этих торговцев совпадут. Вы, наверное,
# не знаете что такое нормирующий коэффициент в Амбере? Это не удивительно…
#
# Пусть торговцу N лет. В стране, откуда он приехал, для расчета операций с денежными единицами,
# действует система счисления с основанием P. Его нормирующим коэффициентом называется сумма цифр
# числа N в системе счисления с основанием P.
#
# Напишите программу, которая покажет, сколько сможет заработать Торговая Гильдия после заключения
# сделки между двумя торговцами.

n1, p1 = map(int, input().split())
n2, p2 = map(int, input().split())

list_ratio_1 = []
list_ratio_2 = []

while n1 > 0:
    list_ratio_1.append(n1 % p1)
    n1 //= p1

while n2 > 0:
    list_ratio_2.append(n2 % p2)
    n2 //= p2

ratio_1 = 0
ratio_2 = 0

for i in range(len(list_ratio_1)):
    ratio_1 += list_ratio_1[i]

for i in range(len(list_ratio_2)):
    ratio_2 += list_ratio_2[i]

if ratio_1 == ratio_2:
    print(ratio_1)
else:
    print(0)
