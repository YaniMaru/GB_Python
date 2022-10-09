# 3 Задайте последовательность чисел. Напишите программу, которая выведет
#  список неповторяющихся элементов исходной последовательности.


def non_repeating_elements(new_list):
    my_list = []
    for i in new_list:
        if new_list.count(i) == 1:
            my_list.append(i)
    print(f"Список из неповторяющихся элементов: {my_list}")


num_list = list(map(int, input("Введите числа через пробел: ").split()))
non_repeating_elements(num_list)
