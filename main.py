import random
# файлы называем входной - input
# выходной - output


def word(str):
    # вход - строка
    # выход - список
    # Выводит список слов
    # return sp
    pass


def unique(sp):
    # вход - список
    # выход - строка
    # находит уникальные слова
    # return un
    pass


def link(sp):
    # вход - список
    # выход - словарь(?)
    # звенья и связи
    # return sl
    # в словаре ключи - слова из un
    # в ключах списки из слов из un, которые с ними связаны
    pass


def start(sp):
    # Стартовые слова
    # вход - список
    # выход - список
    # return st
    pass


def generate(sl, st, n):
    with open('output.txt', 'w'):
        pass
    for j in range(n):
        s = ''
        w = random.choice(st)
        s += w
        if s[-1] in '.!?':
            s = s[:-1]
        s += ' '
        for i in range(19):
            s += random.choice(sl[w])
            if i < 3 and s[-1] in '.!?':
                s = s[:-1]
            if i >= 3 and s[-1] in '.!?':
                break
            s += ' '
        with open('output.txt', 'a') as f:
            f.write(s + ' ')


if __name__ == '__main__':
    generate({'g.': ['g.']}, ['g.'], 3)
    pass
