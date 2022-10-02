# 5 Реализовать алгоритм перемешивания списка.

import random

def shuffle(x):
    x = list(x)
    random.shuffle(x)
    return x


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = shuffle(x)
print(f"Изначальный список: {x}")
print(f"Перемешанный список: {y}")
