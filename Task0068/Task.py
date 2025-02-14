# Мальчик Вася каждый день ездит на метро. Утром он едет в школу, а вечером того же дня, обратно из
# школы, домой. Для того, чтобы немного сэкономить, он покупает электронную смарт-карту на X поездок.
# Когда он хочет зайти в метро, он прикладывает карту к турникету. Если на карте осталось ненулевое
# количество поездок, то турникет пропускает Васю и списывает с карты одну поездку. Если же на
# карте не осталось поездок, то турникет не пропускает Васю, и он (Вася) вынужден купить на этой
# же станции новую карту на X поездок и вновь пройти через турникет.
#
# Вася заметил, что в связи с тем, что утром метро переполнено, покупать новую карту утром накладно
# по времени, и он может опоздать в школу. В связи с этим он хочет понять: будет ли такой день,
# что с утра, поехав в школу, Вася обнаружит у себя на карточке ноль поездок.
#
# Вася больше никуда на метро не ездит и поэтому заходит в метро только на станции около дома и
# на станции около школы.

start_station = input()
x_trips = int(input())

if start_station == 'Home':
    print('Yes')
else:
    if x_trips % 2 == 0:
        print('No')
    else:
        print('Yes')
