# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.


def row(elem, iteration):
    global sum_of_elem
    sum_of_elem += elem
    if iteration != 0:
        elem = elem / -2
        next_iter = iteration - 1
        row(elem, next_iter)


n = int(input('Введите число элементов: '))
sum_of_elem = 0
row(1, n - 1)
print(f'Сумма элементов: {sum_of_elem}')
