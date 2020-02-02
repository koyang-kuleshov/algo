# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]


from collections import deque
from random import choice, randint

hex_nums = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', \
                '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',  \
                'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

n = 10
hexnum1 = ''
hexnum2 = ''
for i in range(randint(1, n)):
    hexnum1 += str(choice(list(hex_nums.keys())))
for i in range(randint(1, n)):
    hexnum2 += str(choice(list(hex_nums.keys())))
print(f'Первое число: {hexnum1}')
print(f'Второе число: {hexnum2}')

def hexsum(num1, num2, hex_dict):
    spam_sum = ''
    in_my_mind = 0
    result = ''
    temp_result = 0
    hex_chars = list(hex_dict.keys())
    num1 = deque(str(num1))
    num2 = deque(str(num2))
    num_size = len(num1) - len(num2)
    if num_size < 0:
        for i in range(abs(num_size)):
            num1.appendleft('0')
    else:
        for i in range(abs(num_size)):
            num2.appendleft('0')
    idx = len(num1) - 1
    while idx >= 0:
        spam_num1 = int(hex_dict[num1[idx]])
        spam_num2 = int(hex_dict[num2[idx]])
        spam_sum = spam_num1 + spam_num2 + in_my_mind
        if spam_sum > 15:
            temp_result = spam_sum - 16
            in_my_mind = 1
            result += hex_chars[temp_result]
        else:
            result += hex_chars[spam_sum]
            in_my_mind = 0
        idx -= 1
        spam_sum = 0
    else:
        if in_my_mind == 1:
            result += '1'
    return result[::-1]

print(f'Сумма чисел: {hexsum(hexnum1, hexnum2, hex_nums)}')

hexnum1 = int(hexnum1, 16)
hexnum2 = int(hexnum2, 16)
test_sum = hex(hexnum1 + hexnum2)
print(f'Проверка:    {str(test_sum)[2:].upper()}')
