#  Напишите программу, которая принимает на вход координаты двух точек и находит
#  расстояние между ними в 2D пространстве.
from math import sqrt


def conculate_Lengt_AB(coorXa, coorYa, coorXb, coorYb):
    lengthAB = sqrt((pow((Xa - Xb), 2) + pow((Ya - Yb), 2)))
    return lengthAB


Xa = float(input('Введите значение Xa: '))
Ya = float(input('Введите значение Ya: '))
Xb = float(input('Введите значение Xb: '))
Yb = float(input('Введите значение Yb: '))


result = conculate_Lengt_AB(Xa, Ya, Xb, Yb)
print(round(result, 2))
