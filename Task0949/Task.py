# Последовательность чисел a1, a2, …, ai,… называется Фибоначчиевой, если для всех i ≥ 3 верно,
# что ai=ai-1+ai-2, то есть каждый член последовательности (начиная с третьего) равен сумме двух предыдущих.
#
# Ясно, что, задавая различные числа a1 и a2, мы можем получать различные такие последовательности,
# и любая Фибоначчиева последовательность однозначно задается двумя своими первыми членами.
#
# Будем решать обратную задачу. Вам будет дано число n и два члена последовательности: an и an+1.
# Вам нужно написать программу, которая по их значениям найдет a1 и a2.

n, a_n, a_n1 = map(int, input().split())
for i in range(n - 1):
    temp = a_n
    a_n = a_n1 - a_n
    a_n1 = temp
print(f'{a_n} {a_n1}')
