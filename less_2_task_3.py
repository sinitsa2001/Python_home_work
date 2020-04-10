'''
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и
вывести на экран. Например, если введено число 3486, надо вывести 6843.

'''


num = input('Введите целое число: ')
num1 = ''
for i in num:
	#print(i)
	num1 = i + num1
print(f'Реверс: {num1}')
#******************************************
num = input('Введите  целое число: ')
num1 = ' '
i = -1
while i >= -1 * len(num):
    num1 = num1 + num[i]
    i = i - 1
print(f'Реверс: {num1}')


#***************************************
a1 = int(input("Введите целое число: "))
a2 = 0

while a1 > 0:
    num = a1 % 10
    a1 = a1 // 10
    a2 = a2 * 10
    a2 = a2 + num

print(f'Реверс: {a2}')


#*****************************************

num = int(input('Введите целое число: '))
num = str(num)

def recurs(n, result):
    size = len(n)
    if size == 0:
        return result
    else:
        result += n[(len(n) - 1):]
        n = n[:(len(n) - 1)]
        return recurs(n, result)

print(recurs(num, "Реверс:"))
#****************************************