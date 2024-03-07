# На стандартной шахматной доске 8х8 заданы координаты двух клеток. Требуется определить:
# имеют ли данные клетки одинаковый цвет?

def get_color(num1: int, num2: int) -> str:
    color = ''
    if num1 % 2 == 0 and num2 % 2 == 0:
        color = 'black'
    elif num1 % 2 == 0 and num2 % 2 != 0:
        color = 'white'
    elif num1 % 2 != 0 and num2 % 2 == 0:
        color = 'white'
    elif num1 % 2 != 0 and num2 % 2 != 0:
        color = 'black'
    return color


x1, y1, x2, y2 = map(int, input().split())
color1 = get_color(x1, y1)
color2 = get_color(x2, y2)
if color1 == color2:
    print('YES')
else:
    print('NO')
    