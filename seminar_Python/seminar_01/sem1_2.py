# 2. Найти максимальное из пяти чисел.

list = [80, 154, 6, 5, 98]


def find_max_value(list):
    index = 0
    max_index = len(list)-1
    max = list[0]
    while index <= max_index:
        if list[index] > max:
            max = list[index]
        index += 1
    return max


print(find_max_value(list))
