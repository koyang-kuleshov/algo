# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран
# исходный и отсортированный массивы. Сортировка должна быть реализована в виде
# функции. По возможности доработайте алгоритм (сделайте его умнее).
from random import randint


def arr_sort(obj):
    spam_pos = 1
    eggs_replace = False
    while spam_pos < len(obj):
         for i in range(len(obj)-spam_pos):
            last_idx = len(obj) - i - 1
            last_of_last_idx = len(obj) - i - 2
            if obj[last_idx] > obj[last_of_last_idx]:
                   obj[last_idx], obj[last_of_last_idx] = obj[last_of_last_idx], obj[last_idx]
                   eggs_replace = True
         if not eggs_replace:
               return obj
         spam_pos += 1
    return obj


n = 10
arr = [ randint(-100, 100) for _ in range(n) ]
# arr2 = arr_sort(sorted(arr) Проверка на отсортированный массив
arr2 = arr_sort(arr.copy())

print(arr, arr2, sep='\n')
