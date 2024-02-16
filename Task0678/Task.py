# Шулер показывает следующий трюк. Он имеет три одинаковых наперстка. Под первый (левый) он кладет маленький шарик. Затем он очень быстро выполняет ряд перемещений наперстков, каждое из которых – это одно из трех перемещений - A, B, C:
#
# A - обменять местами левый и центральный наперстки,
# B - обменять местами правый и центральный наперстки,
# C - обменять местами левый и правый наперстки.
# Необходимо определить, под каким из наперстков окажется шарик после всех перемещений.

combination = input()
ball = [1, 0, 0]
for i in range(len(combination)):
    if combination[i] == 'A':
        temp = ball[0]
        ball[0] = ball[1]
        ball[1] = temp
    elif combination[i] == 'B':
        temp = ball[2]
        ball[2] = ball[1]
        ball[1] = temp
    if combination[i] == 'C':
        temp = ball[2]
        ball[2] = ball[0]
        ball[0] = temp
for i in range(len(ball)):
    if ball[i] == 1:
        print(f'{i + 1}')
        