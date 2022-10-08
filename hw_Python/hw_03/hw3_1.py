# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт
#  сумму элементов списка, стоящих на нечётной позиции. *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def sum_elements_odd_positions(my_list):
    res = 0
    for i in range(len(my_list)):
        if i % 2 != 0:
            res += my_list[i]
    print(f'Сумма элементов списка, стоящих на нечётных позициях : {res}')


def sum_of_odd(input_list):
    res = 0
    for i in range(1, len(input_list), 2):
        #  i % 2:
        if i % 2 != 0:    
            res += input_list[i]
    print(f'Сумма элементов списка, стоящих на нечётных позициях : {res}')


list_num = [2, 3, 5, 9, 3]
sum_elements_odd_positions(list_num)
sum_of_odd(list_num)
