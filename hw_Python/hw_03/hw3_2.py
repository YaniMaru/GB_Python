# 2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];      - [2, 3, 5, 6] => [12, 15]

def multiply_pair_num(list1):
    result_list = []
    for i in range((len(list1)+1)//2):
        result_list.append(list1[i]*list1[len(list1)-1-i])
    return result_list


my_list = [2, 3, 4, 5, 6]
print(multiply_pair_num(my_list))
