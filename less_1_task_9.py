
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

# вариант решения № 1
a = float(input('Ведите число а: '))
b = float(input('Ведите число b: '))
c = float(input('Ведите число c: '))

if b < a and a < c:
    print(f'middle = {a}')
elif b < c:
    print(f'middle = {c}')
else:
    print(f'middle = {b}')
if b > a and a > c:
    print(f'middle = {a}')
elif b > c:
    print(f'middle = {c}')
else:
    print(f'middle = {b}')


# Вариант решения № 2 (более компактный)


a = float(input('Ведите число а: '))
b = float(input('Ведите число b: '))
c = float(input('Ведите число c: '))
if b < a < c or c < a < b:
    print(f'middle = {a}')
elif a < b < c or c < b < a:
    print(f'middle = {b}')
else:
    print(f'middle = {c}')






