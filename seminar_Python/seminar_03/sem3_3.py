# 3 Напишите программу, которая определит позицию второго вхождения строки в списке либо
# сообщит, что её нет.  Пример:
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3

# Задание списка строк
def input_string():
    list_string = input(f"Введите список строк (строки через пробел) ")
    list_string = list_string.split(' ')
    return list_string


list_string = input_string()
print(f'Список строк {list_string}')
string_find = input(f"Введите строку, которую надо найти в списке ")

if list_string.count(string_find) > 1:
    position = list_string.index(string_find)
    # print(f'Позиция первого вхождения {position}')
    position = list_string.index(string_find, position + 1)
    print(f'Позиция второго вхождения {position}')
else:
    print(-1)
