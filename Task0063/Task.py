# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого
# Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

s, p = map(int, input().split())
x, y = 0, 0
for i in range(s):
    if i * (s - i) == p:
        x = i
        y = s - i
        break
print(f'{x} {y}')