# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции. *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def sum_elements_odd_positions(list):
    sum = 0
    for i in range(len(list)):
        if i % 2 != 0:
            sum += list[i]
    print(f'Сумма элементов списка, стоящих на нечётных позициях : {sum}')


list_num = [2, 3, 5, 9, 3]
sum_elements_odd_positions(list_num)
