# На клеточном поле N•M расположены две жёсткие детали. Деталь A накрывает в каждой строке несколько
# (не ноль) первых клеток, деталь B — несколько (не ноль) последних; каждая клетка либо полностью накрыта
# одной из деталей, либо нет.
#
# Деталь B начинают двигать влево, не поворачивая, пока она не упрётся в A хотя бы одной клеткой. Определите,
# на сколько клеток будет сдвинута деталь B.

n, m = map(int, input().split())
result = m
for i in range(n):
    my_str = input()
    if result > my_str.count('.'):
        result = my_str.count('.')
print(result)