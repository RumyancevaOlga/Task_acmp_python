# На большом поле находятся суслик и собака. Собака хочет суслика съесть, а суслик хочет оказаться в
# безопасности, добежав до одной из норок, выкопанных в поле. Ни собака, ни суслик в математике не сильны,
# но, с другой стороны, они и не беспросветно глупы. Суслик выбирает определенную норку и бежит к ней по прямой
# с определенной скоростью. Собака, которая очень хорошо понимает язык телодвижений, угадывает, к какой норке бежит
# суслик, и устремляется к ней со скоростью вдвое большей скорости суслика. Если собака добегает до норки первой
# (раньше суслика), то она съедает суслика; иначе суслик спасается.
#
# Требуется написать программу, которая поможет суслику выбрать норку, в которой он может спастись, если таковая
# существует.
import math

xs, ys = map(int, input().split())
xd, yd = map(int, input().split())
n = int(input())
for i in range(n):
    xn, yn = map(int, input().split())
    ss = math.sqrt(((xn - xs) ** 2) + ((yn - ys) ** 2))
    sd = math.sqrt(((xn - xd) ** 2) + ((yn - yd) ** 2))
    if sd / 2 >= ss:
        print(i + 1)
        break
else:
    print('NO')