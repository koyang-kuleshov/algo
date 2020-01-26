# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MAX_ITEM = 100
MIN_ITEM = 0

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')

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
array[min_pos], array[max_pos] = max_elem, min_elem
print(f'Новый массив: {array}')
