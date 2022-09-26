# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30.

num = int(input('Введите целое число: '))


def find(number):
    if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
        return "Число кратно"
    return "Число не кратно"


print(find(num))
