# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных
# индексов. *Пример:*  - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


def fibonacci(num):
    fbn_num = []
    n1, n2 = 1, 1
    for _ in range(num):
        fbn_num.append(n1)
        n1, n2 = n2, n1 + n2
    n1, n2 = 0, 1
    for _ in range(num + 1):
        fbn_num.insert(0, n1)
        n1, n2 = n2, n1 - n2
    return fbn_num


number = int(input('Введите число: '))
print(fibonacci(number))
