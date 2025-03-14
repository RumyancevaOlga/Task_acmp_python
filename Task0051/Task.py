# Определение 1:
#
# n!!...!=n(n-k)(n-2k)...(n mod k), если n не делится на k,
#
# n!!...!=n(n-k)(n-2k)...k, если n делится на k (знаков ! в обоих случаях k штук).
#
# Определение 2:
#
# X mod Y — остаток от деления X на Y.
#
# Например, 10 mod 3 = 1; 3! = 3•2•1; 10!!! = 10•7•4•1;
#
# Мы по заданным n и k смогли вычислить значение выражения из определения 1. А вам слабо?

n, k = map(str, input().split())

n = int(n)
k = len(k)

factorial = 1

for i in range(0, n, k):
    factorial *= n
    n -= k

print(factorial)
