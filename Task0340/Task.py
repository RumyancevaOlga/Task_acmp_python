# На столе лежат коробка размера A1 × B1 × C1 и коробка размера A2 × B2 × C2.
# Выясните можно ли одну из этих коробок положить в другую, если разрешены повороты коробок вокруг
# любого ребра на угол 90 градусов.

list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))
list_1.sort()
list_2.sort()
if list_1 == list_2:
    print('Boxes are equal')
elif list_1[0] >= list_2[0] and list_1[1] >= list_2[1] and list_1[2] >= list_2[2]:
    print('The first box is larger than the second one')
elif list_1[0] <= list_2[0] and list_1[1] <= list_2[1] and list_1[2] <= list_2[2]:
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')
