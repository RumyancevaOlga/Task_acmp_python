my_string = input()


def gen_fib(len_string):
    fib_list = []
    fib_1 = 1
    fib_2 = 1
    while len_string >= fib_2:
        fib_list.append(fib_1)
        temp = fib_2
        fib_2 = fib_1 + fib_2
        fib_1 = temp
    fib_list.append(fib_1)
    fib_list.pop(0)
    return fib_list


list_to_print = gen_fib(len(my_string))

for i in range(len(list_to_print)):
    print(my_string[list_to_print[i] - 1], end='')
