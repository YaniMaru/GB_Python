# 1.Напишите программу, которая принимает на вход вещественное число и показывает
# сумму его цифр. *Пример:*  - 6782 -> 23      - 0,56 -> 11

def sum_num(num):
    number = num.replace(".", "")
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    print(f'Сумма всех цифр в числе равна {sum}')


def sum_num2(num):
    sum = 0
    for i in float_number:
        if i != '.' and i != ',':
            sum += int(i)
    print(f'Сумма всех цифр в числе равна {sum}')


float_number = input("Введите вещественное число: ")
sum_num(float_number)
sum_num2(float_number)
