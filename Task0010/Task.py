# Вася в школе изучил квадратные уравнения и понял, как они легко решаются путем
# вычисления дискриминанта. Но Петя поведал ему о методе решения кубических уравнений
# вида A*X3 + B*X2 + C*X + D = 0. На факультативе по математике Васе задали решить около
# ста уравнений как раз такого вида. Но, к сожалению, Вася забыл формулы, о которых рассказывал ему Петя.
# Но Васе было известно, что все корни уравнений – целые числа и находятся на отрезке [-100, 100].
# Поэтому у Васи есть шанс найти их методом перебора, но для этого ему придется затратить уйму времени,
# т.к. возможно необходимо будет осуществить перебор нескольких тысяч значений. Помогите Васе написать программу,
# которая поможет ему найти корни кубических уравнений!

import math

a, b, c, d = map(int, input().split())
list_result = []
for i in range(-100, 101):
    if a * math.pow(i, 3) + b * (i ** 2) + c * i + d == 0:
        list_result.append(i)
for i in range(len(list_result)):
    print(list_result[i], end=' ')
