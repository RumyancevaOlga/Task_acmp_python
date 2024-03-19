# В галактике «Milky Way» на планете «Snowflake» есть N городов, некоторые из которых соединены дорогами.
# Император галактики «Milky Way» решил провести инвентаризацию дорог на планете «Snowflake». Но,
# как оказалось, он не силен в математике, поэтому он просит вас сосчитать количество дорог.
# Требуется написать программу, помогающую императору сосчитать количество дорог на планете «Snowflake».

n = int(input())
list_town = []
for i in range(n):
    list_town.append(list(map(int, input().split())))
roads = 0
for i in range(len(list_town)):
    for j in range(len(list_town[i])):
        if list_town[i][j] == 1:
            roads += 1
print(f'{int(roads / 2)}')
