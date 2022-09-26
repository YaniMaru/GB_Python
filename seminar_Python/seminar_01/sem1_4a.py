# 4. Показать первую цифру дробной части числа. (методом строк)

def first_float():
    n = input('Введите вещественное число: ')
    n_list = n.split('.')
    print(n_list[1][0])


first_float()
