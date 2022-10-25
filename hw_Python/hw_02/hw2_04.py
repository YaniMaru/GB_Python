# 4 Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение
# элементов на указанных позициях. Позиции хранятся в списке positions -
# создайте этот список (например: positions = [1, 3, 6]).

def get_list(n):
    list = []
    for i in range(-n, n + 1):
        list.append(i)
    return (list)


n = int(input('Введите целое число: '))
positions = [1, 3, 6]
result = 1
for i in range(0, len(positions)):
    result *= get_list(n)[positions[i]]

print(f'Список: {get_list(n)}')
print(f'Произведение элементов на указанных позициях {positions}= {result}')
