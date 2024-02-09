# Задано время отправления поезда и время в пути до конечной станции.
# Требуется написать программу, которая найдет время прибытия этого поезда (возможно, в другие сутки).
import datetime

hour_1, minute_1 = map(int, input().split(':'))
hour_2, minute_2 = map(int, input().split())

time_start = datetime.datetime(hour=hour_1, minute=minute_1, second=0, year=2024, month=2, day=9)
time_delta = datetime.timedelta(hours=hour_2, minutes=minute_2, seconds=0)
time_stop = time_start + time_delta
print('{:%H:%M}'.format(time_stop))
