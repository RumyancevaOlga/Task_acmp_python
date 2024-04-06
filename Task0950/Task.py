# Последовательность из символов «0» и «1» называется бинарной. Они широко применяются в информатике
# и других науках. Одно из неудобств бинарных последовательностей – их трудно запоминать. Для решения
# этой проблемы были предложены разные способы их сжатия. Программист Слава использует следующий способ:
# просматривая последовательность слева направо, он заменяет «1» на «a», «01» на «b», «001» на «c», …,
# «00000000000000000000000001» на «z». Напишите программу, которая поможет Славе автоматизировать этот способ сжатия.

my_list = input()
result = []
count = 0
for i in range(len(my_list)):
    if my_list[i] == '0':
        count += 1
    else:
        result.append(chr(97 + count))
        count = 0
for i in range(len(result)):
    print(f'{result[i]}', end='')
    