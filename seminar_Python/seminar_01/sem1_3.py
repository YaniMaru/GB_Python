# 3. Вывести на экран числа от -N до N.

num = int(input('Введите целое число: '))


def print_num(number):
    number = abs(number)  # модуль числа
    first = number * -1
    second = number
    while first < second:
        print(f'{first},', end='')
        first += 1
    print(num)


print_num(num)
