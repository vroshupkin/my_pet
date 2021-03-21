import sqlite3
import datetime

today = datetime.date.today()


def db_insert_into_constructor(table_name, *args):
    output = '''INSERT INTO %s''' % table_name
    output += " VALUES ("
    for s in args:
        output += "'" + s + "', "
    output = output[:-2]
    output += ')'
    cur.execute(output)


def db_commit_and_exit():
    con.commit()
    con.close()


def db_print_row(table_name, *args):
    text = "SELECT "
    for row_name in args:
        text += row_name + ", "
    text = text[:-2]
    text += " FROM " + table_name

    for row in cur.execute(text):
        print(row)


con = sqlite3.connect('vocabulary.db')
cur = con.cursor()

db_print_row('Vadim', 'word', 'translate', 'date')

#db_insert_into_constructor('Vadim', 'provide', 'предоставлять, обеспечивать', str(today))
con.execute('''CREATE UNIQUE INDEX idx_word ON Vadim (word);''')
db_commit_and_exit()

if __name__ == '__main__':
    pass


