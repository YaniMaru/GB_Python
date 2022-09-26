# 1. По двум заданным числам проверить является ли одно квадратом второго.

number_first = int(input('Введите первое число '))
number_second = int(input('Введите первое число '))
if number_first == number_second**2:
    print((f'Число {number_first} являетя квадратом числа {number_second}'))
else:
    print((f'Число {number_first} не являетя квадратом числа {number_second}'))
