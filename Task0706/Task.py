# В начале координат установлена пушка, стреляющая шариками для пинг-понга. На некотором расстоянии
# R от нее, параллельно оси ОХ, находится кирпичная стена бесконечной длины. Между стеной и осью OX
# расположена точечная цель с координатами (X,Y). Требуется нацелить пушку так, чтобы шарик ударился
# сначала о стену, а затем попал в цель. Определите кратчайшее расстояние от оси OY до точки соударения
# шарика со стеной.

r, x, y = map(int, input().split())
result = r * abs(x) / (2 * r - y)
print(round(result, 2))
