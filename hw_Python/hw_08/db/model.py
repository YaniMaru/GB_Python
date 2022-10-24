from data_base import *


def distribution(choice_user):
    if (choice_user == '1'):
        preview_base()
    elif (choice_user == '2'):
        add_record()
    elif (choice_user == '3'):
        find_record(input('Введите фамилию для поиска: '))
    elif (choice_user == '4'):
        delete_record(int(input('Введите id для удаления записи: ')))
    elif (choice_user == '5'):
        change_salary(int(input('Введите id: ')), int(
            input('Введите новый размер заработной платы: ')))
    elif (choice_user == '6'):
        change_bonus(int(input('Введите id: ')), int(
            input('Введите новый размер премии: ')))
    elif (choice_user == '7'):
        print('Всего хорошего!')
    else:
        print('Введите корректное число')


def preview_base():
    print()
    for i in cursor.execute('SELECT * FROM personal'):
        print(*i)
    print()


def add_record():
    base = [input("Введите фамилию сотрудника: "),
            input("Введите имя сотрудника: "),
            input("Введите должность сотрудника: "),
            int(input("Введите зарплату сотрудника: ")),
            int(input("Введите премию сотрудника: "))]
    cursor.execute(
        'INSERT INTO personal(last_name, first_name, position, salary,bonus) VALUES (?,?,?,?,?)', base)
    db.commit()


def find_record(text):
    cursor.execute('SELECT * FROM personal WHERE last_name LIKE (?)', (text,))
    one = cursor.fetchall()
    print()
    for i in one:
        print(*i)
    print()
    return one


def delete_record(id):
    cursor.execute('DELETE FROM personal WHERE id=:n;', {"n": id})
    db.commit()


def change_salary(id, num):
    cursor.execute('UPDATE personal SET salary=:num WHERE id=:n;', {
                   "num": num, "n": id})
    db.commit()


def change_bonus(id, num):
    cursor.execute('UPDATE personal SET bonus=:num WHERE id=:n;', {
                   "num": num, "n": id})
    db.commit()
