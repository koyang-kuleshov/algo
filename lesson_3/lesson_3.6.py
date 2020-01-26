# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
import random

SIZE = 10
MAX_ITEM = 10
MIN_ITEM = 0

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')
spam_sum = 0

min_elem = array[0]
max_elem = array[0]
min_pos = 0
max_pos = 0

for count, item in enumerate(array):
    if min_elem > item:
        min_elem = item
        min_pos = count
    elif max_elem < item:
        max_elem = item
        max_pos = count
print(f'Минимальны элемент array[{min_pos}] = {min_elem}')
print(f'Максимальный элемент array[{max_pos}] = {max_elem}')
for item in array[min_pos: max_pos]:
    spam_sum += item
print(f'Сумма элементов между минимальным и максимальным числами: {spam_sum}')
