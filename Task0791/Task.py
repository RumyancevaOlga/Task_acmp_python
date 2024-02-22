# Клетки шахматной доски пронумерованы числами от 1 до 64 по строкам слева направо и снизу вверх. Напишите программу, которая по заданному номеру клетки определяет номера всех клеток,
# имеющих с ней общую сторону.

num = int(input())
# desk = [[1, 2, 3, 4, 5, 6, 7, 8],
#         [9, 10, 11, 12, 13, 14, 15, 16],
#         [17, 18, 19, 20, 21, 22, 23, 24],
#         [24, 26, 27, 28, 29, 30, 31, 32],
#         [33, 34, 35, 36, 37, 38, 39, 40],
#         [41, 42, 43, 44, 45, 46, 47, 48],
#         [49, 50, 51, 52, 53, 54, 55, 56],
#         [57, 58, 59, 60, 61, 62, 63, 64]]
# i = 0
# f = 0
# if num < 8:
#     for j in range(len(desk[0])):
#         if num == desk[0][j]:
#             i = j
#     if 1 < num < 8:
#         print(f'{desk[0][i - 1]} {desk[0][i + 1]} {desk[1][i]}')
#     elif num == 1:
#         print(f'{desk[0][i + 1]} {desk[1][i]}')
#     elif num == 8:
#         print(f'{desk[0][i - 1]} {desk[1][i]}')
# elif 8 < num < 57:
#     for j in range(len(desk)):
#         for k in range(len(desk[j])):
#             if num == desk[j][k]:
#                 i = k
#                 f = j
#     if num % 8 == 1:
#         print(f'{desk[f - 1][i]} {desk[f][i + 1]} {desk[f + 1][i]}')
#     elif num % 8 == 0:
#         print(f'{desk[f - 1][i]} {desk[f][i - 1]} {desk[f + 1][i]}')
#     else:
#         print(f'{desk[f - 1][i]} {desk[f][i - 1]} {desk[f][i + 1]} {desk[f + 1][i]}')
# else:
#     for j in range(len(desk[7])):
#         if num == desk[7][j]:
#             i = j
#     if 57 < num < 64:
#         print(f'{desk[6][i]} {desk[7][i - 1]} {desk[7][i + 1]}')
#     elif num == 57:
#         print(f'{desk[6][i]} {desk[7][i + 1]}')
#     elif num == 64:
#         print(f'{desk[6][i]} {desk[7][i - 1]}')

if 1 < num < 8:
    print(f'{num - 1} {num + 1} {num + 8}')
if num == 1:
    print(f'{num + 1} {num + 8}')
if num == 8:
    print(f'{num - 1} {num + 8}')
if 8 < num < 57 and num % 8 != 1 and num % 8 != 0:
    print(f'{num - 8} {num - 1} {num + 1} {num + 8}')
if 8 < num < 57 and num % 8 == 1:
    print(f'{num - 8} {num + 1} {num + 8}')
if 8 < num < 57 and num % 8 == 0:
    print(f'{num - 8} {num - 1} {num + 8}')
if 57 < num < 64:
    print(f'{num - 8} {num - 1} {num + 1}')
if num == 57:
    print(f'{num - 8} {num + 1}')
if num == 64:
    print(f'{num - 8} {num - 1}')
