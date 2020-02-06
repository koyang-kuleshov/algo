# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах в рамках первых трех уроков. Проанализировать результат и определить
# программы с наиболее эффективным использованием памяти
from sys import getsizeof
from random import choice

# 2.3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.


def show_size(*objects):
    spam_size = getsizeof(objects)
    for obj in objects:
        if hasattr(obj, '__iter__'):
            if hasattr(obj, 'items'):
                for key, value in obj.items():
                    show_size(key)
                    show_size(value)
                    spam_size += getsizeof(obj)
            elif not isinstance(obj, str):
                for item in obj:
                    show_size(item)
                    spam_size += getsizeof(obj)
            else:
                spam_size += getsizeof(obj)
        else:
            spam_size += getsizeof(obj)
    return spam_size


# Алгоритм №1
def get_str1(temp_str):
    obj_size = 0
    if isinstance(temp_str, int):
        temp_str = str(temp_str)
    str2 = ''
    len_str1 = len(temp_str)
    if len(str2) != len_str1 and len(temp_str) > 1:
        str2 += temp_str[len(temp_str) - 1:]
        get_str1(temp_str[:len(temp_str) - 1])
    else:
        str2 += temp_str
    obj_size += show_size(str2, len_str1, temp_str)
    return obj_size

# Алгоритм №2
def get_str2(num_2):
    if isinstance(num_2, str):
        num_2 = int(num_2)
    result = 0
    while num_2 > 0:
        result = result * 10 + num_2 % 10
        num_2 = num_2 // 10
    return show_size(result, num_2)


n = 10
str_to_reverse = ''
for i in range(n):
    str_to_reverse += str(choice(list({1, 2, 3, 4, 5, 6, 7, 8, 9, 0})))

print(f'Реализация №1: {get_str1(str_to_reverse)} байт') # 209 байт
print(f'Реализация №2: {get_str2(str_to_reverse)} байт') # 120 байт
print(f'Реализация №3: {show_size(str_to_reverse[::-1])} байт') # 115 байт

# Вывод:
# Наиболее эффективным оказалась встроенная функция, хотя и алгоритм №2 позазал
# себя сравнительно не плохо. Функция №1 из-за многократного вызова и передачи
# аргументов требует больше всего памяти.
