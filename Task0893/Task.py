# В соревнованиях по хоккею участвует N команд. Сколько существует вариантов распределения
# комплектов золотых, серебряных и бронзовых медалей, если одно призовое место может
# занять только одна команда?

# from math import factorial

n = int(input())
medals = 3

# result = factorial(n) / factorial(n - medals)

result = 1

if n == 2:
    result += 1

if n >= 3:
    for i in range(n - medals + 1, n + 1):
        result *= i

print(result)
