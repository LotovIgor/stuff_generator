import random
# файлы называем входной - input
# выходной - output


# Оля
def word(str):
    # вход - строка
    # выход - список
    # Выводит список слов в том порядке, в котором они были в тексте
    # return sp
    pass


# Арсений
def unique(sp):
    # вход - список
    # выход - строка
    # находит уникальные слова
    # return un
    pass


def start(sp):
    # Стартовые слова
    # вход - список
    # выход - список
    # return st
    pass


# Игорь
def link(sp, un):
    # вход - список
    # выход - словарь
    # звенья и связи
    # return sl
    # в словаре ключи - слова из un
    # в ключах списки из слов из un, которые с ними связаны
    sl = {i:[] for i in un}
    # print(sl)
    for i in range(len(sp) - 1):
            sl[sp[i]].append(sp[i + 1])
    return sl


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
            if sl[w] == []:
                w = random.choice(st)
            else:
                w = random.choice(sl[w])
            s += w
            if i < 3 and s[-1] in '.!?':
                s = s[:-1]
            if i >= 3 and s[-1] in '.!?':
                break
            s += ' '
        if s[-1] not in '.!?':
            s = s[:-1]
            s += '.'
        with open('output.txt', 'a') as f:
            f.write(s + ' ')


if __name__ == '__main__':
    # generate({'g.': ['g.']}, ['g.'], 3)
    sp = ['Hello,', 'my', 'name', 'is', 'Igor', 'I', 'am', 'Igor', 'Igor', 'is', 'me']
    un = ['Hello,', 'my', 'name', 'is', 'Igor', 'I', 'am', 'Igor', 'is', 'me']
    st = ['Hello,', 'Igor', 'I', 'Igor']
    n = 5
    # print(link(sp, un))
    generate(link(sp, un), st, n)
