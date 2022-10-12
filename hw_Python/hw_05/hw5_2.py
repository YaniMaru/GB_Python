# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать
# не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний
# ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у
# своего конкурента?

from random import randint


def input_dat(player):
    x = int(
        input(f'{player}, сколько конфет вы возьмете? (от 1 до 28) '))
    while x < 1 or x > 28:
        x = int(input(f'{player}, введите корректное количество конфет: '))
    return x


player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')
value = int(input('Введите количество конфет на столе: '))
turn = randint(0, 2)
print('Первый ход делает', end=' ')
print(player1 if turn else player2)
while value > 27:
    if turn:
        value -= input_dat(player1)
        turn = False
        print(f"На столе осталось: {value} конфет(а)")
    else:
        value -= input_dat(player2)
        turn = True
        print(f"На столе осталось: {value} конфет(а)")

print('Победитель', end=' ')
print(player1 if turn else player2)
