# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import namedtuple


Company = namedtuple('Company', 'name quart_1, quart_2, quart_3, quart_4 year')
company_count = int(input('Введите количество компаний: '))
companys = [0 for _ in range(company_count)]
profit_sum = 0

for i in range(company_count):
    name = input(f'Введите название {i+1}-й компании: ')
    quarts = [float(j) for j in input('Введите через запятую прибыль в каждом квартале: ').split(',')]

    year = 0
    for quart in quarts:
        year += quart
    profit_sum += year
    companys[i] = Company(name, *quarts, year)
    print(f'Справка: {companys[i]}')

if company_count == 1:
    print(f'Всего одна компания: {companys[0].name}. Eё прибыль в год: {companys[0].year}')

else:
    profit_average = profit_sum / company_count

    small = []
    large = []

    for i in range(company_count):

        if companys[i].year < profit_average:
            small.append(companys[i])

        elif companys[i].year > profit_average:
            large.append(companys[i])

    print(f'\nСредняя годовая прибыль по компаниям: {profit_average: .2f}')

    print(f'Компания с прибылью меньше чем: {profit_average: .2f}:')
    for data in small:
        print(f'Компания "{data.name}" ->> прибыль {data.year: .2f}')

    print(f'\nКомпания, с прибылью больше чем:  {profit_average: .2f}:')
    for data in large:
        print(f'Компания "{data.name}" ->> прибыль {data.year: .2f}')