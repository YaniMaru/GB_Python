# 3.Задайте список из вещественных чисел. Напишите программу, которая найдёт
#  разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*   [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]

max_value, min_value = 0, 1
for i in my_list:
    if (divmod(i, 1))[1] > max_value:
        max_value = divmod(i, 1)[1]
    elif (divmod(i, 1))[1] < min_value and (divmod(i, 1))[1] != 0:
        min_value = (divmod(i, 1))[1]
print(round(max_value - min_value, 2))
