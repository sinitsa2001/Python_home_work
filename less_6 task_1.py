'''
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
● написать 3 варианта кода (один у вас уже есть);
● проанализировать 3 варианта и выбрать оптимальный;
● результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
● написать общий вывод: какой из трёх вариантов лучше и почему.
Надеемся, что вы не испортили программы, добавив в них множество sys.getsizeof после каждой переменной,
а проявили творчество, фантазию и создали универсальный код для замера памяти.

'''
'''
!! Предисловие к решению задачи. 
а) Во первых: воспользуюсь кодом(программкой) любезно предоставленной преподавателем. 
б) во вторых: не уверен что все правильно понял...поэтому буду "лепить горбатого"..вы уж извините..
но...тут ведь надо понимать = цели и задачи.. Программистом мне стать не светит ибо: 
уже стар для этого, к тому же = не мой уровень..я уже давно являюсь работодателем...и вот для реализации нового направления
в бизнесе хочу говорить на одном языке с людьми которым буду платить ЗП.. (на самом деле уже плачу и плАчу..и довольно давно)
извиняюсь за лирику.
про уровень...прошу не воспринимаь на свой счет...мэтры не в счет))
ниже (по течению)..я взял Вашу задачку (решение) и ваш код для замеров...а еще ниже = свое решение...вот и буду сравнивать ..
!! 64 разряда!!  иными словами = то что у вас 12...у меня = 24
'''
'''
import sys

from collections import deque

BASE = 16

HEX_NUMBERS = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
               'A', 'B', 'C', 'D', 'E', 'F')

BIN_NUMBERS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}

def sum_hex(first, second):

    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))

    result = deque()
    overflow = 0
    while len(first) != 0:
        first_num = BIN_NUMBERS[first.pop()]
        second_num = BIN_NUMBERS[second.pop()]

        result_num = first_num + second_num + overflow

        if result_num >= BASE:
            overflow = 1
            result_num -= BASE
        else:
            overflow = 0

        result.appendleft(HEX_NUMBERS[result_num])

    if overflow == 1:
        result.appendleft('1')

    return result


def mult_hex(first, second):
    first = first.copy()
    second = second.copy()

    if len(second) > len(first):
        first, second = second, first

    second.extendleft('0' * (len(first) - len(second)))
    result = deque('0')

    while len(second) != 0:
        second_num = BIN_NUMBERS[second.pop()]

        spam = deque('0')
        for _ in range(second_num):
            spam = sum_hex(spam, first)

        spam.extend('0' * (len(first) - len(second) - 1))
        result = sum_hex(result, spam)

    return result


a = deque(input('Введите первое число в hex формате (только цифры от 0 до f): ').upper())
b = deque(input('Введите второе число в hex формате (только цифры от 0 до f): ').upper())

# z = hex(int('a2', 16) + int('c4f', 16)) - плохой подход на два балла
print(f'{list(a)} + {list(b)} = {list(sum_hex(a, b))}')
print(f'{a} * {b} = {mult_hex(a, b)}')  # специально убрал список, чтобы показать как хранится



#print(sys.getrefcount(a))
#print(sys.getrefcount('eegrwegerg'))
#print(sys.getsizeof(a))

def show(x):
    print(f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show(key)
                show(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)


show(BIN_NUMBERS)
show(HEX_NUMBERS)
'''
'''
замерил словарь - и он (ожиданно) больше чем кортеж : 
type=<class 'dict'>, size=656, obj={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
* далее выборочно : содержимое словаря: 
строчные ожидаемо больше : размер 50
type=<class 'str'>, size=50, obj=0
цифры, соответственно меньше (0  = 24)
type=<class 'int'>, size=28, obj=1
Общий размер словаря со его содержимым: 1246 байт
В кортеже меньше данных поэтому его размер меньше...но он и сам занимает меньше места 
type=<class 'tuple'>, size=184, obj=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
т.е = 800 байт содержимое + 184 сам кортеж...984 байта
Вывод можно сделать такой...
словарь больше по факту, но в нем  и больше информации в два раза...а размер его не в два раза больше, 
значит, при прочих равных если бы мы использовали кортеж для реализации задачи = вероятно было бы меньше занято памяти, но
решение задачи (на большом объеме входящей информации) было бы быстрее с испольованием словаря..
ну и посмотрел сколько на что ссылок.. = 0 = победитель безусловный!! 

'''

import sys, struct, ctypes
def show(x):
    print(f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}, count= {sys.getrefcount(x)}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show(key)
                show(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)


from collections import deque


def summ_hex(x, y):
    my_dict = {a: str(a) for a in range(10)}
    my_dict.update({str(a): a for a in range(10)})
    my_dict.update({'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'})
    show(my_dict)
    show(num1) #type=<class 'list'>, size=112, obj=['2', 'A'] +100 (данные) = 212 байт
    #show(num2)
    result = deque()
    numeric = 0


    if len(y) > len(x):
        x, y = deque(y), deque(x)

    else:
        x, y = deque(x), deque(y)
    show(deque(x)) #type=<class 'collections.deque'>, size=640, obj=deque(['C', '4', 'F']) + 150 сами данные

    while x:

        if y:
            res = my_dict[x.pop()] + my_dict[y.pop()] + numeric

            #print(numeric)

        else:
            res = my_dict[x.pop()] + numeric

            #print(numeric)

        numeric = 0

        if res < 16:
            result.appendleft(my_dict[res])
           # print(result)

        else:
            result.appendleft(my_dict[res - 16])
            numeric = 1
            #print(result)

    if numeric:
        result.appendleft('1')
        #print(result)

    return list(result)

'''
Вот замер второй задачи(первой половины)
в этом варианте все входящие данные в виде словаря..и что мы видим: 
type=<class 'dict'>, size=1192, obj={0: '0', и т.д = !! только сам словарь (без содержимого) весит почти столько же сколько 
сколько в предыдущем варианте решения = словарь с кортежем и со всем содержимым... 
само содержимое в моей реализации (корявой): строчные 1600 байт, цифры = 892 байта, но
надо понимать что и строчные и цифры повторяются два раза, ибо не смог найти более элегантного решения чтобы при 
использовании словаря = ключ = значение были все данные и 0-15 и все буквы (в значениях и в ключах) потому и повтор. 
а это все большой вес.
общий размер всего содержимого: 3684 байта...что аж почти в 3 раза тяжелее.
вывод. 
а) надо вытащить базовые данные за пределы функции - что позволит ускорить само быстродействие функции
б) оптимизировать входящие данные в сторону уменьшения - как минимум с использованием кортежей и словаря.
в) НЕ использовать решение с множеством ибо знаем что множество будет еще тяжелее.
'''

def multi_hex(x, y):
    my_dict = {a: str(a) for a in range(10)}
    my_dict.update({str(a): a for a in range(10)})
    my_dict.update({'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'})
    result = deque()
    spam = deque([deque() for _ in range(len(y))])
    #show(spam)

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = my_dict[y.pop()]
        #print(m)

        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * my_dict[x[j]])
            #print(spam)

        for _ in range(i):
            spam[i].append(0)
            #print(spam)

    numeric = 0

    for _ in range(len(spam[-1])):
        res = numeric

        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()

        if res < 16:
            result.appendleft(my_dict[res])

        else:
            result.appendleft(my_dict[res % 16])
            numeric = res // 16

    if numeric:
            result.appendleft(my_dict[numeric])

    return list(result)

num1 = list(input('Введите 1-е число: ').upper())
num2 = list(input('Введите 2-е число: ').upper())

print(*num1, '+', *num2, '= ', *summ_hex(num1, num2))

print(*num1, '*', *num2, '=', *multi_hex(num1, num2))
