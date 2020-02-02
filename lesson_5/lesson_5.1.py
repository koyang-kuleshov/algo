# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и
# отдельно вывести наименования предприятий, чья прибыль ниже среднего.


from collections import namedtuple
import random


def firm_profit(frst_qtr, scnd_qtr, thrd_qtr, frth_qtr):
    return frst_qtr + scnd_qtr + thrd_qtr + frth_qtr


lst = list()
profit = 0
avg_profit = 0
Firm = namedtuple('Firm', 'name, first_qrt, second_qrt, third_qrt, fourth_qrt, \
    firm_profit')
n = int(input('Введите количество фирм: '))

for count, i in enumerate(range(n), 1):
    name = input(f'Введите название фирмы №{count}: ')
    frst_spam = random.randint(30000000, 100000000) / 100
    scnd_spam =random.randint(30000000, 100000000) / 100
    thrd_spam =random.randint(30000000, 100000000) / 100
    frth_spam =random.randint(30000000, 100000000) / 100
    lst.append(Firm(name, frst_spam, scnd_spam, thrd_spam, frth_spam, firm_profit(
        frst_spam, scnd_spam, thrd_spam, frth_spam)))
    profit += frst_spam + scnd_spam + thrd_spam + frth_spam

avg_profit = profit / n

print(f'Средняя прибыль компаний {avg_profit}. Компании у которых прибыль выше \
    средней: ')
for i in lst:
    if i.firm_profit > avg_profit:
        print(i.name)
print('Компании у которых прибыль ниже средней')
for i in lst:
    if i.firm_profit <= avg_profit:
        print(i.name)

