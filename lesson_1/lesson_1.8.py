# 8. Определить, является ли год, который ввел пользователем, високосным или не високосным.
year = int(input('Введите год для проверки в формате YYYY: '))
if year % 400 == 0:
    print(f'{year} год - високосный')
elif year % 4 == 0 and year % 100 != 0:
    print(f'{year} год - високосный')
else:
    print(f'{year} год - не високосный')

