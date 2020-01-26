# 4. Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 10
MAX_ITEM = 10
MIN_ITEM = 0

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')

spam_quantity = 0
eggs_number = 0
for i in array:
    temp_quantity = 0
    for j in array:
        if i == j:
            temp_quantity += 1
    if spam_quantity < temp_quantity:
        spam_quantity = temp_quantity
        eggs_number = i
print(f'Число {eggs_number} встречается {spam_quantity} раз')
