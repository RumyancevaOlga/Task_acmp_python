# Задана последовательность, состоящая только из символов
# ‘>’, ‘<’ и ‘-‘. Требуется найти количество стрел, которые
# спрятаны в этой последовательности. Стрелы – это подстроки вида ‘>>-->’ и ‘<--<<’.

my_string = input()

left_arrow = '<--<<'
right_arrow = '>>-->'

left_arrow_count = 0
right_arrow_count = 0

for i in range(len(my_string) - 4):
    if my_string[i] == left_arrow[0]:
        if my_string[i + 1] == left_arrow[1]:
            if my_string[i + 2] == left_arrow[2]:
                if my_string[i + 3] == left_arrow[3]:
                    if my_string[i + 4] == left_arrow[4]:
                        left_arrow_count += 1
    if my_string[i] == right_arrow[0]:
        if my_string[i + 1] == right_arrow[1]:
            if my_string[i + 2] == right_arrow[2]:
                if my_string[i + 3] == right_arrow[3]:
                    if my_string[i + 4] == right_arrow[4]:
                        right_arrow_count += 1

print(left_arrow_count + right_arrow_count)
