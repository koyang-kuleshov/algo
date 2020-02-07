# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
# и отсортированный массивы.

from random import randint


n = int(input( 'Введите величину массива: ' ))
arr = [randint(100, 5000) / 100 for _ in range(n)]

def merge_sort(obj):
    middle = len(obj) // 2
    left = obj[:middle]
    right = obj[middle:]
    if len(obj) <= 2:
        return obj
    else:
        for i in range(len(left) - 1):
            if left[i] > left[i + 1]:
                left[i], left[i + 1] = left[i + 1], left[i]
        for j in range(len(right) - 1):
            if right[j] > right[j + 1]:
                right[j], right[j + 1] = right[j + 1], right[j]
        left = merge_sort(left)
        right = merge_sort(right)
        if len(left) == len(right):
            min_len = len(left)
        elif len(left) < len(right):
            min_len = len(left)
        else:
            min_len = len(right)
        # min_len = min_len if min_len % 2 == 0 else min_len - 1
        result = conc_arr(left, right)
        return result

def conc_arr(larr, rarr):
    rst = []
    if len(larr) < len(rarr):
        larr = [*larr, *[float('inf') * len(rarr) - len(larr)]]
    elif len(larr) > len(rarr):
        rarr = [*rarr, *[float('inf') * len(larr) - len(rarr)]]
    larr_idx = 0
    rarr_idx = 0
    y = 0
    for i in range(len(larr)):
        if larr[larr_idx] < rarr[rarr_idx]:
            rst.append(larr[larr_idx])
            larr_idx += 1
        elif larr[larr_idx] > rarr[rarr_idx]:
            rst.append(rarr[rarr_idx])
            rarr_idx += 1
    if len(larr) - larr_idx <= 0:
        rst = [*rst, *rarr[rarr_idx:]]
    elif larr_idx == rarr_idx:
        if larr[larr_idx] < rarr[rarr_idx]:
            rst.append( larr[larr_idx] )
            rst.append( rarr[rarr_idx] )
        else:
            rst.append( rarr[rarr_idx] )
            rst.append( larr[larr_idx] )
    else:
        rst = [*rst, *larr[larr_idx:]]
    return rst

print(f'Исходный массив:        {arr}')
print(f'Отсортированный массив: {merge_sort(arr.copy())}')
