# У студента-филолога Васи есть замечательный друг Петя.
# И Петя никак не может выучить английский язык. Английский текст Петя еще кое-как читает,
# но пишет с ужасными ошибками, причем чаще всего он вставляет в слова лишние буквы.
#
# Вася решил помочь Пете. Теперь каждый день Вася диктует Пете слова, а Петя их записывает.
# После семестра занятий Петя стал писать много лучше и теперь делает в словах только по одной ошибке.
# Чтобы автоматизировать процесс исправления ошибок, Вася просит Вас написать программу, которая удаляет
# из слова одну лишнюю букву и показывает Пете правильное слово.

number, word = input().split()
number = int(number) - 1
result = word[:number] + word[number + 1:]
print(result)
