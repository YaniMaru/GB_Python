# Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

num_list = list(map(int, input('Введите числа через пробел: ').split()))
new_list = [i for i in num_list if num_list.count(i) == 1]
print(f'Список из неповторяющихся элементов: {new_list}')

# Прошлый вариан:

# def non_repeating_elements(new_list):
#     my_list = []
#     for i in new_list:
#         if new_list.count(i) == 1:
#             my_list.append(i)
#     print(f"Список из неповторяющихся элементов: {my_list}")


# num_list = list(map(int, input("Введите числа через пробел: ").split()))
# non_repeating_elements(num_list)
