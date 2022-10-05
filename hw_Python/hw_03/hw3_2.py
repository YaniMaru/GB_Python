# 2.Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];      - [2, 3, 5, 6] => [12, 15]

def multiply_pair_num(list):
    result_list = []
    for i in range((len(list)+1)//2):
        result_list.append(list[i]*list[len(list)-1-i])
    return result_list


list = [2, 3, 4, 5, 6]
print(multiply_pair_num(list))
