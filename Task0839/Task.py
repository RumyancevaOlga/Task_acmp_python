# Всем известно, что многие олимпиадные задачи начинаются со слов «Всем известно».
# Но мало кто знает, что начинающему программисту Паше такие задачи меньше всего нравятся.
# Потому что обычно после слов «всем известно» описывается такой факт, о котором он даже не догадывался.
# После очередной подобной задачи Паша решил проверить, а действительно ли всем известно, что сумма первых
# N нечетных чисел равняется N2:
# Для этого Паша провел опрос всех людей, попавшихся ему под руку в известной социальной сети.
# Результаты опроса он записал в текстовый файл. Он ставил цифру один, если человеку был действительно
# известен данный факт, в противном случае в файл записывался нуль. Все было хорошо, пока Паша не открыл
# файл и не ужаснулся, увидев длинную последовательность из единичек. Как же он теперь будет искать среди них нули?
#
# Уже всем известно, что Паша – начинающий программист, поэтому для обработки результатов исследования
# он обратился к вам за помощью.

n = input()
for i in range(len(n)):
    if n[i] == '0':
        print('NO')
        break
else:
    print('YES')
