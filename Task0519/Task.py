# Требуется написать программу, которая найдет наименьшее и наибольшее числа, состоящие из тех же цифр, что и заданное
# натуральное число N.
#
# Входной файл INPUT.TXT содержит натуральное число N (N ≤ 2×109).
#
# Выходной файл OUTPUT.TXT должен содержать в одной строке наименьшее, а через пробел – наибольшее числа.

n = input()
num_list = []

for i in range(len(n)):
    num_list.append(int(n[i]))


min_num = 0
max_num = 0

min_list = sorted(num_list)
max_list = sorted(num_list, reverse=True)

if min_list[0] == 0:
    temp = 0
    i = 0
    while temp == 0:
        temp = min_list[i + 1]
        i += 1
    min_list[0] = temp
    min_list[i] = 0

for i in range(len(n)):
    min_list[i] = str(min_list[i])
    max_list[i] = str(max_list[i])

min_text = ''.join(min_list)
max_text = ''.join(max_list)

min_num = int(min_text)
max_num = int(max_text)

print(min_num, max_num)
