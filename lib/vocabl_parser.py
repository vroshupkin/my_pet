with open('../doc/vocabl.txt', encoding='utf-8') as f:
    text = f.read()


print(text)

# TODO разобрать на слово, транскрипцию, перевод, добавлено ли в базу данных
# TODO перезаписать файл в структуре: [15]-[15]-[50]-[1]. Добавить пробелов по формуле (15-len(word))%4, tab=len(a)//4