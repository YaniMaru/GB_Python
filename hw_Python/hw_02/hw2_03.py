# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
#  *Пример:*    Для n = 6:  [2.0, 2.25, 2.3704, 2.4414, 2.4883, 2.5216]
#               Сумма чисел = 14.0717


def get_list(n):
    list = []
    for n in range(1, num + 1):
        list.append(round((1 + 1 / n)**n, 4))
    return list


num = int(input('Введите число n: '))
print(f'Список для n = {num}: {get_list(num)}')
print(f'Сумма чисел = {sum(get_list(num))}')
