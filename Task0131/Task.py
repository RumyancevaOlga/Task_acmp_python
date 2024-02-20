# В доме живет N жильцов. Однажды решили провести перепись всех жильцов данного дома и составили
# список, в котором указали возраст и пол каждого жильца. Требуется найти номер самого старшего
# жителя мужского пола.

n = int(input())
max_years = 0
num = -1
for i in range(1, n + 1):
    years, gender = map(int, input().split())
    if years > max_years and gender == 1:
        num = i
        max_years = years
print(num)
