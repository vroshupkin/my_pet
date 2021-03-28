import sqlite3
import datetime
today = datetime.date.today()


# TODO DONE Вносит в table, значения values
def db_insert_into(table, *args):
    values = ', '.join(args)
    output = f'''INSERT INTO {table} VALUES ({values});'''

    cur.execute(output)

# Необходимость функции не ясна
def db_commit_and_exit():
    con.commit()
    con.close()


# TODO DONE Функция будет использоваться для CLI
def db_print_row(table, *args):
    values = ', '.join(args)
    text = f"SELECT {values} FROM {table}"

    for row in cur.execute(text):
        print(row)


# TODO Читает все значения в таблице и вносит в двухмерный массив
def db_load_table(table, *args):

    text = f"SELECT {', '.join(args)} FROM {table}"

    out = []
    for row in cur.execute(text):
        out.append(row)
    return out


# TODO DONE
def db_add_column(table_name, column_name, type='text'):
    con.execute(f'''ALTER TABLE {table_name} ADD COLUMN {column_name} {type}''')


# TODO Сделать
def copy_table(new_table_name, copy_table_name, *args):
    pass


# TODO Так как нету функции прямого удаление через ALTER TABLE, удалить с помощью копирования
def db_delete_column(table_name, column_name):
    pass


if __name__ == '__main__':
    con = sqlite3.connect('vocabulary.db')
    cur = con.cursor()

    # print(f"Test 1: db_print_row('Vadim', 'word', 'translate', 'date')\n\tOut:", end="")
    # db_print_row('Vadim', 'word', 'translate', 'date')

    # db_print_row('Vadim', 'word')

    # con.execute('''CREATE UNIQUE INDEX idx_word ON Vadim (word);''')



    table = db_load_table('Vadim', 'word')
    print(table)
    con.close()

# TODO vocabulary.db Добавить колонку транскрипции
# TODO achivments.db Создать, добавить колонки date, time, descriptions, hashtags
# TODO history db, Узнать как дела с историей у SQLite
# TODO сделать удаленный сервер SQLite
# TODO Сделать CLI команду добавление слова в словарь


