# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#
# Требуется найти N-е число Фибоначчи.

n = int(input())
f1 = 0
f2 = 1
if n == 0:
    print('0')
elif n == 1:
    print('1')
else:
    result = 0
    i = 0
    while i != n:
        result = f1 + f2
        if i % 2 == 0:
            f2 = result
        else:
            f1 = result
        i += 1
    print(result)
