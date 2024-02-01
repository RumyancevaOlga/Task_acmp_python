# Кондиционер
# (Время: 1 сек. Память: 16 Мб Сложность: 12%)
# В офисе, где работает программист Петр, установили кондиционер нового типа. Этот кондиционер отличается особой простотой в управлении. У кондиционера есть всего лишь два управляемых параметра: желаемая температура и режим работы.

# Кондиционер может работать в следующих четырех режимах:

# «freeze» — охлаждение. В этом режиме кондиционер может только уменьшать температуру. Если температура в комнате и 
# так не больше желаемой, то он выключается.
# «heat» — нагрев. В этом режиме кондиционер может только увеличивать 
# температуру. Если температура в комнате и так не меньше желаемой, то 
# он выключается.
# «auto» — автоматический режим. В этом режиме кондиционер может как 
# увеличивать, так и уменьшать температуру в комнате до желаемой.
# «fan» — вентиляция. В этом режиме кондиционер осуществляет только 
# вентиляцию воздуха и не изменяет температуру в комнате.
# Кондиционер достаточно мощный, поэтому при настройке на правильный 
# режим работы он за час доводит температуру в комнате до желаемой.

# Требуется написать программу, которая по заданной температуре в 
# комнате troom, установленным на кондиционере желаемой температуре 
# tcond и режиму работы определяет температуру, которая установится в 
# комнате через час.

# Входные данные
# Первая строка входного файла INPUT.TXT содержит два целых числа troom 
# и tcond, разделенных ровно одним пробелом 
# (–50 ≤ troom ≤ 50, –50 ≤ tcond ≤ 50).

# Вторая строка содержит одно слово, записанное строчными буквами 
# английского алфавита — режим работы кондиционера, как указано выше.

# Выходные данные
# Выходной файл OUTPUT.TXT должен содержать одно целое число — 
# температуру, которая установится в комнате через час.

t_room, t_cond = map(int, input().split())
mode = input()
if mode == 'freeze':
    result = min(t_room, t_cond)
elif mode == 'heat':
    result = max(t_room, t_cond)
elif mode == 'auto':
    result = t_cond
elif mode == 'fan':
    result = t_room
print(result)