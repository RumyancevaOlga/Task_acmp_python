data = int(input())
a = data % 10
data = data // 10
b = data % 10
data = data // 10
c = data % 10
data = data // 10
d = data % 10
data = data // 10
e = data % 10
data = data // 10
f = data % 10
data = data // 10
if a + b + c == d + e + f:
    print('YES')
else:
    print('NO')
