# Требуется найти самую длинную непрерывную цепочку нулей в последовательности нулей и единиц.

n = input()
count = 0
j = 0
for i in range(len(n)):
    if n[i] == '0':
        j += 1
    else:
        if count < j:
            count = j
        j = 0
else:
    if count < j:
        count = j
print(count)
