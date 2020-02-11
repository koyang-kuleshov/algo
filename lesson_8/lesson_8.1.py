# Определить количество различных подстрок с использованием хеш-функции.
# Задача: на вход функции дана строка, требуется вернуть количество различных
# подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком


import hashlib


def rabin_karp(s, t):
    num_str = 0
    len_sub = len(t)
    h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()
    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i+len_sub].encode('utf-8')).hexdigest():
            num_str += 1
    print(f'Строка "{t}" содержиться {num_str} раз')
    return num_str


def num_subs(spam_str):
    counter = 0
    lst_str = list(spam_str)
    eggs = set()
    eggs_elem = ''
    word = 1
    i = 0
    while word < len(spam_str):
        j = i + 1
        while i < len(spam_str) and j <= len(spam_str):
            if i == 0 and j == 4:
                break
            eggs_elem = str(''.join(lst_str[i:j]))
            if eggs_elem not in eggs:
                eggs.add(eggs_elem)
                counter += rabin_karp(spam_str, eggs_elem)
            j += 1
        i += 1
        word += 1
    return counter


src_str = 'ab ba'
src_str = src_str.replace(' ', '')
print(f'Всего в строке "{src_str}" содержится {num_subs(src_str)} подстрок')
