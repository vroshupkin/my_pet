import sqlite3
import datetime
today = datetime.date.today()


# TODO DONE
def db_insert_into(table_name, *args):
    values = ', '.join(args)
    output = f'''INSERT INTO {table_name} VALUES ({values});'''

    cur.execute(output)


def db_commit_and_exit():
    con.commit()
    con.close()


# TODO DONE Функция будет использоваться для CLI
def db_print_row(table_name, *args):
    values = ', '.join(args)
    text = f"SELECT {values} FROM {table_name}"

    for row in cur.execute(text):
        print(row)


# TODO DONE
def db_add_column(table_name, column_name, type='text'):
    con.execute(f'''ALTER TABLE {table_name} ADD COLUMN {column_name} {type}''')


# TODO Сделать
def copy_table(new_table_name, copy_table_name, *args):
    pass


# TODO Так как нету функции прямого удаление через ALTER TABLE, удалить с помощью копирования
def db_delete_column(table_name, column_name):
    pass





con = sqlite3.connect('vocabulary.db')
cur = con.cursor()



#con.execute('''CREATE UNIQUE INDEX idx_word ON Vadim (word);''')

# db_add_column('Vadim', 'Transcription')

db_print_row('Vadim', 'word')
db_commit_and_exit()


def test_print_row():
    db_print_row('Vadim', 'word', 'translate', 'date')


if __name__ == '__main__':
    db_print_row('Vadim', 'word', 'translate', 'date')

# TODO vocabulary.db Добавить колонку транскрипции
# TODO achivments.db Создать, добавить колонки date, time, descriptions, hashtags
# TODO history db, Узнать как дела с историей у SQLite
# TODO сделать удаленный сервер SQLite
# TODO Сделать CLI команду добавление слова в словарь


