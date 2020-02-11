# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
# две равные части: в одной находятся элементы, которые не меньше медианы, в
# другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не
# рассматривался на уроках.


from random import randint
from math import floor


def gnome_sort(arr):
    i = 1
    while i < len(arr):
        if not i or arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
    return arr


m = 4
arr = [randint(0, 10) for _ in range(2 * m + 1)]
print(f'Исходный массив:        {arr}')
print(f'Отсортированный массив: {gnome_sort(arr)}')
# FIXIT: change functions for round
mediana = arr[floor(len(arr) / 2)]
print(f'Медиана массива {mediana} на позиции {arr.index(mediana)}')

