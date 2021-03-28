import sqlite3
from database import db_insert_into, db_load_table

current_db = 'vocabl.db'

# TODO parser vocabl.txt


with open('doc/vocabl.txt', encoding='utf-8') as f:
    vocabl_text = f.read()


# Slice text use separator and add to arr
def separate_text(text, sep='\n'):
    arr = []
    ind_1 = 0
    ind_2 = 0
    for i in range(len(text)):
        if text[i] == sep:
            ind_2 = i
            arr.append(text[ind_1:ind_2])
            ind_1 = ind_2 + 1
    return arr


# Удаляет все символы del_letter
def del_letter(text, del_lett=" "):
    while del_lett in text:
        i = text.find(del_lett) + 1
        text = text[:i-1] + text[i:]
    return text


def del_empty_iteam(arr):
    l = len(arr)
    i = 0
    while True:
        if arr[i] == '':
            arr.pop(i)
            i -= 1
        if i == len(arr) - 1:
            break
        i += 1



arr = separate_text(vocabl_text)

# TODO Добавить vocabl.txt в базу данных                                            [1]
# TODO Сделать add.txt, который будет добавлять новые слова в базу данных           [2]
# TODO Сделать функцию создающую из базы данных текстовый файл                      [3]
# TODO Сделать edit строки
# TODO [1] + [2] + [3] = ver. 0.01 версия минимального функционала1йё
for a in arr:
    if len(arr) > 1:
        word = a[:21]
        transcription = a[21:50]
        translation = a[50:120]
        state = a[120:123]

    print(word, transcription, translation, state)
#print(arr)


# TODO make real error
# TODO DONE Сделать для двумерного массива
class Table:
    def __init__(self, inp_data, inp_ident=[20, 20, 20]):
        self.data = inp_data
        self.ident = inp_ident

    def __str__(self):
        text = ""
        for row in self.data:
            i = 0
            for elem in row:
                ident_num = self.ident[i] - len(elem)
                text += elem + (ident_num * ' ')
                if i != (len(self.ident) - 1):
                    i += 1
            text += "\n"
            i = 0
        return text





def test_table():
    inp_data = [['provide', '[prəˈvīd]', 'предоставлять', '+'], ['then', '[THen]', 'тогда', '-']]
    inp_ident = [20, 20, 30]

    con = sqlite3.connect('vocabulary.db')
    cur = con.cursor()
    db_load_table.cur = cur
    a = db_load_table('Vadim')
    print(a)

    con.close()

test_table()

# TODO Прочитать для базу данных в двумерный массив
