# 2. Во втором массиве сохранить индексы четных элементов первого массива.

import random

SIZE = 10
MAX_ITEM = 100
MIN_ITEM = 0

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')
second_array = list()

for count, item in enumerate(array):
    if item % 2 == 0:
        second_array.append(count)

print(f'Индексы второго массива: {second_array}')
