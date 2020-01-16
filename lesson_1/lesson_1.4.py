# 4. Написать программу, которая генерирует в указанных пользователем границах
# случайное целое число,
# случайное вещественное число,
# случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random
low_limit = input('Введите нижнюю границу: ')
high_limit = input('Введите верхнюю границу: ')
task = input('Что нужно сгенерировать: целое число(i) вещественное число(f) '
             'случайный символ(s): ')
if task.lower() == 'i':
    result = random.randint(int(low_limit), int(high_limit))
elif task.lower() == 'f':
    result = random.random() * int(low_limit) * int(high_limit) * 10
else:
    low_limit = ord(low_limit)
    high_limit = ord(high_limit)
    result = chr(random.randint(low_limit, high_limit))
print(f'Результат: {result}')
