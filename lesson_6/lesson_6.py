# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах в рамках первых трех уроков. Проанализировать результат и определить
# программы с наиболее эффективным использованием памяти
from timeit import timeit

# 2.3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

# Алгоритм №1
def get_str1(temp_str):
    str2 = ''
    len_str1 = len(temp_str)
    if len(str2) != len_str1 and len(temp_str) > 1:
        str2 += temp_str[len(temp_str) - 1:]
        get_str1(temp_str[:len(temp_str) - 1])
    else:
        str2 += temp_str
    # print(f'Число {temp_str} в обратном порядке - {str2}')
# str1 = input('Введите число: ')
print(timeit('get_str1("1234")', number=100, globals=globals()))
# 0.00012478299686335959
print(timeit('get_str1("12345678")', number=100, globals=globals()))
# 0.00028283000210649334
print(timeit('get_str1("1234567812345678")', number=100, globals=globals()))
# 0.0005897980008739978
print(timeit('get_str1("12345678123456781234567812345678")', number=100, globals=globals()))
# 0.0012418559999787249
print(timeit('get_str1("1234567812345678123456781234567812345678123456781234567812345678")', number=100, globals=globals()))
# 0.0023380669990729075

print('-'*100)

# Алгоритм №2
# num = int(str1)
def get_str2(num_2):
    result = 0
    while num_2 > 0:
        result = result * 10 + num_2 % 10
        num_2 = num_2 // 10
print(timeit('get_str2(1234)', number=100, globals=globals()))
# 4.179600000497885e-05
print(timeit('get_str2(12345678)', number=100, globals=globals()))
# 9.166699965135194e-05
print(timeit('get_str2(1234567812345678)', number=100, globals=globals()))
# 0.00022185600028024055
print(timeit('get_str2(12345678123456781234567812345678)', number=100, globals=globals()))
# 0.00047755099876667373
print(timeit('get_str2(1234567812345678123456781234567812345678123456781234567812345678)', number=100, globals=globals()))
# 0.001069234000169672

print('-'*100)

# Алгоритм №3
print(timeit('resule2 = "1234"[::-1]', number=100, globals=globals()))
# 7.406000804621726e-06
print(timeit('resule2 = "12345678"[::-1]', number=100, globals=globals()))
# 7.680002454435453e-06
print(timeit('resule2 = "1234567812345678"[::-1]', number=100, globals=globals()))
# 1.6488997061969712e-05
print(timeit('resule2 = "123456781234567812345678"[::-1]', number=100, globals=globals()))
# 8.413000614382327e-06
print(timeit('resule2 = "123456781234567812345678123456781234567812345678"[::-1]', number=100, globals=globals()))
# 1.905599856399931e-05

# Вывод: Несмотря на то, что я доработал свою первый алгоритм - избавился от глобальных
# переменных, он всё равно оказался медленнее, чем вариант 2 и вариант 3.
# Я думаю можно немного улучшить 1ый вариант, если вычислять длинну строки вне
# функции и потом передавать в функцию. Так как len вызывается 78 раз.
