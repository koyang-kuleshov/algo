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
    if len(obj) <= 1:
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
        result = conc_arr(left, right)
        return result

def conc_arr(larr, rarr):
    rst = []
    larr_idx = 0
    rarr_idx = 0
    while larr_idx < len(larr) and rarr_idx < len(rarr):
        if larr[larr_idx] < rarr[rarr_idx]:
            rst.append(larr[larr_idx])
            larr_idx += 1
        elif larr[larr_idx] > rarr[rarr_idx]:
            rst.append(rarr[rarr_idx])
            rarr_idx += 1
    if len(larr) - larr_idx == 0:
        rst = [*rst, *rarr[rarr_idx:]]
    elif len(rarr) - rarr_idx == 0:
        rst = [*rst, *larr[larr_idx:]]
    return rst

print(f'Исходный массив:        {arr}')
print(f'Отсортированный массив: {merge_sort(arr.copy())}')
