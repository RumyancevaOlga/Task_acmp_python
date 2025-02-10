# Уравнение для пятиклассников представляет собой строку
# длиной 5 символов. Второй символ строки является либо знаком '+' (плюс) либо '-'
# (минус), четвёртый символ — знак '=' (равно). Из первого, третьего и пятого
# символов ровно два являются цифрами из диапазона от 0 до 9, и один — буквой x, обозначающей неизвестное.
#
# Требуется написать программу, которая позволит решить данное уравнение относительно x.

equation = input()

a = equation[0]
sign = equation[1]
b = equation[2]
equal = equation[3]
c = equation[4]

result = 0

if a == 'x':
    if sign == '+':
        result = int(c) - int(b)
    else:
        result = int(c) + int(b)

if b == 'x':
    if sign == '+':
        result = int(c) - int(a)
    else:
        result = int(a) - int(c)

if c == 'x':
    if sign == '+':
        result = int(a) + int(b)
    else:
        result = int(a) - int(b)

print(result)
