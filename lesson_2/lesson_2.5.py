# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

start = 32
for i in range(10):
    end = start + 10
    row = ''
    for count, item in enumerate(range(start, end), start):
        if item <= 127:
            row +=  f'{count} - {chr(item)} '
        else:
            break
    print(row)
    start = end
