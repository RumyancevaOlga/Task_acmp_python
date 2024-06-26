# В доме Вилли установили скоростной лифт новой экспериментальной модели. В этом лифте кнопки с номерами
# этажей заменены двумя другими кнопками. При нажатии на первую кнопку лифт поднимается на один этаж вверх,
# а при нажатии на вторую – опускается на один этаж вниз.
#
# Младшему брату Вилли Дилли очень нравится кататься на новом лифте. Он катается на нём до тех пор, пока не побывает
# на каждом из этажей хотя бы по одному разу. После этого Дилли довольный возвращается домой.
#
# Зная порядок, в котором Дилли нажимал на кнопки лифта, попробуйте определить общее количество этажей в доме Вилли
# и Дилли.

n = input()
result = 0
max_ = 0
min_ = 0
for i in range(len(n)):
    if n[i] == '1':
        result += 1
    else:
        result -= 1
    if result > max_:
        max_ = result
    if result < min_:
        min_ = result
print(max_ - min_ + 1)
