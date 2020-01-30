# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;

# Использовать алгоритм решето Эратосфена

from timeit import timeit
import cProfile

def iteration_func(elem):
    simple = 4
    first = (2, 3, 5, 7)
    find_elem = first[3]
    number_check = True
    if elem <= 4:
        return first[elem -1]
    else:
        while elem > simple:
            find_elem += 1
            for i in first:
                if find_elem % i == 0:
                    number_check = False
                    break
            if number_check:
                simple += 1
            number_check = True
    return find_elem


def eratosthenes(elem):
    n = elem * 3
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    # print(b[elem - 1])

print(timeit('iteration_func(5)', number=100, globals=globals()))
# 7.072599692037329e-05
print(timeit('iteration_func(10)', number=100, globals=globals()))
# 0.000335466000251472
print(timeit('iteration_func(20)', number=100, globals=globals()))
# 0.0009312889997090679
print(timeit('iteration_func(40)', number=100, globals=globals()))
# 0.0024880749988369644
print(timeit('iteration_func(80)', number=100, globals=globals()))
# 0.005240195001533721
print(timeit('iteration_func(8000)', number=100, globals=globals()))
# 0.5455646439986594

cProfile.run('iteration_func(30)')
         # 4 function calls in 0.000 seconds

   # Ordered by: standard name

   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        # 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        # 1    0.000    0.000    0.000    0.000 lesson_4.2.py:9(iteration_func)
        # 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        # 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(timeit('eratosthenes(5)', number=100, globals=globals()))
# 0.00035997699887957424
print(timeit('eratosthenes(10)', number=100, globals=globals()))
# 0.0006988589993852656
print(timeit('eratosthenes(20)', number=100, globals=globals()))
# 0.0012358720014162827
print(timeit('eratosthenes(40)', number=100, globals=globals()))
# 0.002475773999321973
print(timeit('eratosthenes(80)', number=100, globals=globals()))
# 0.004970158999640262
print(timeit('eratosthenes(8000)', number=100, globals=globals()))
# 0.6735784320007951

cProfile.run('eratosthenes(30)')
         # 28 function calls in 0.000 seconds

   # Ordered by: standard name

   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        # 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        # 1    0.000    0.000    0.000    0.000 lesson_4.2.py:29(eratosthenes)
        # 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       # 24    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        # 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод: Первый вариант реализации алгоритма показывает себя лучше возможно из-за
# того, что не работает со списком.
