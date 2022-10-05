# 4.Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*   - 45 -> 101101        - 3 -> 11       - 2 -> 10


def binary(num):
    result = ''
    while num > 0:
        result = str(num % 2) + result
        num = num // 2
    return result


number = int(input('Введите число: '))
print(f'Двоичное число: {binary(number)}')
