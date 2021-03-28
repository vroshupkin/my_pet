import hashlib


def get_sha1(file_path):
    with open(file_path) as f:
        text = f.read()

    text = bytes(text, encoding='utf-8')
    m = hashlib.sha1(text)
    return m.hexdigest()


def test_sha1(path):
    print(get_sha1(path))


test_sha1('vocabulary.db')


