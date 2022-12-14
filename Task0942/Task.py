# Олимпиада
# (Время: 1 сек. Память: 16 Мб Сложность: 2%)
# Трое студентов, пятикурсник, третьекурсник и первокурсник, живут в одной комнате общежития и любят участвовать 
# в соревнованиях по программированию по правилам ACM. У каждого из них свой подход к решению задач. 
# Пятикурсник решает все задачи строго по порядку - сначала первую, затем вторую, и так до последней. 
# Третьекурсник решает задачи строго в обратном порядке – сначала последнюю, затем предпоследнюю, и так до первой. 
# А первокурсник сначала решает самую простую задачу, затем – самую простую из оставшихся задач, 
# и так до самой сложной. Сложность задачи определяется временем, необходимым для её решения. 
# Для решения одной и той же задачи наши студенты тратят одинаковое количество времени.

# Ваша задача – по описанию соревнований по программированию определить, кто из студентов победит. 
# Напомним, что по правилам ACM побеждает участник, за 300 минут решивший больше всего задач, 
# а при равенстве количества задач – набравший меньше штрафного времени.

# Наши студенты – очень сильные программисты, и при решении задач они не делают неправильных попыток. 
# Поэтому за задачу начисляется штраф в размере количества минут от начала соревнования до её посылки на проверку. 
# Если же и количество штрафного времени совпадает – то студент со старшего курса уступает победу студенту 
# с младшего курса.

# Входные данные
# Первая строка входного файла INPUT.TXT содержит натуральное число N (N ≤ 10) – количество задач. 
# Во второй строке записаны через пробел N натуральных чисел – количество минут, необходимое для решения каждой задачи. 
# Время решения задачи не превосходит 300 минут.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите номер курса студента, одержавшего победу в олимпиаде.

# with open('INPUT.txt', 'r') as my_f:
#     data = my_f.readlines()

# task_number = data[0].strip()
# time = data[1].split()

# fifth_count = 0
# fifth_student = 0

# for i in range(int(task_number)):
#     if fifth_student + int(time[i]) <= 300:
#         fifth_student = fifth_student + int(time[i])
#     else:
#         break
#     fifth_count += 1

# third_count = 0
# third_student = 0

# for i in range(int(task_number)):
#     if third_student + int(time[len(time) - i - 1]) < 300:
#         third_student = third_student + int(time[len(time) - i - 1])
#     else:
#         break
#     third_count += 1

# for i in range(int(task_number)):
#     time[i] = int(time[i])
# time.sort()

# first_count = 0
# first_student = 0

# for i in range(int(task_number)):
#     if first_student + time[i] <= 300:
#         first_student = first_student + time[i]
#     else:
#         break
#     first_count += 1

# winner = 5
# if third_count >= fifth_count and third_count > first_count:
#     winner = 3
# elif first_count >= fifth_count and first_count >= third_count:
#     winner = 1 

# with open('OUTPUT.txt', 'w') as my_f1:
#     my_f1.write(str(winner))

with open('OUTPUT.txt', 'w') as my_f1:
    my_f1.write(str(1))