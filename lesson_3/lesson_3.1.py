# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9. [In the range of natural numbers from 2 to 99, determine how many of them are multiples of each of the numbers in the range from 2 to 9.]
import random

SIZE = 10
MAX_ITEM = 99
MIN_ITEM = 2

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Исходный массив: {array}')
# for count, item in enumerate(array):
for i in range(2,10):
    eggs_sum = 0
    for item in array:
        if item % i == 0:
            eggs_sum += 1
    print(f'Чисел кратных {i} - {eggs_sum}')
