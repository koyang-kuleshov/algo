# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
num = input('Введите трёхзначное число ')
num_1 = num // 100
num_2 = (num - (num_1 * 100)) // 10
num_3 = num % 10
sum_of_num = num_1 + num_2 + num_3
prod_of_num = num_1 * num_2 * num_3
print(f'Сумма чисел: {sum_of_num}')
print(f'Произведение чисел: {prod_of_num}')
