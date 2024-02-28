# Заданы площадь кольца и радиус внешней окружности. Требуется определить радиус внутренней окружности.

import math

S, R1 = map(float, input().split())
S_all = math.pi * (R1 ** 2)
R2 = round(math.sqrt((S_all - S) / math.pi), 3)
print(R2)
