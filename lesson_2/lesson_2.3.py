# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.


def get_str2(temp_str):
    global str2
    if len(str2) != len_str1 and len(temp_str) > 1:
        str2 += temp_str[len(temp_str) - 1:]
        get_str2(temp_str[:len(temp_str) - 1])
    else:
        str2 += temp_str


str2 = ''
str1 = input('Введите число: ')
len_str1 = len(str1)
get_str2(str1)
print(f'Число {str1} в обратном порядке - {str2}')
