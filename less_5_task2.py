'''
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections
(пусть это и не очевидно с первого раза. Вы же не Голландец ;-).
'''

#A2 и C4F

#print(hex(1501091))
#print(hex(940569))
'''
my_dict = {a :str(a) for a in range(10)}
my_dict.update({str(a): a for a in range(10)})
my_dict.update({'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'})

print(my_dict)
'''
a = 'A2'
b = 'C4F'
c = hex(int(a, 16)+ int(b, 16))
e = hex(int(a, 16)* int(b, 16))
print (c)
print(e)
# !! Я так понимаю = это не решение))??

from collections import deque


def summ_hex(x, y):
    my_dict = {a: str(a) for a in range(10)}
    my_dict.update({str(a): a for a in range(10)})
    my_dict.update({'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'})
    #print(my_dict)
    #print(num1,num2)
    result = deque()
    numeric = 0


    if len(y) > len(x):
        x, y = deque(y), deque(x)

    else:
        x, y = deque(x), deque(y)
    #print(deque(x))
    #print(deque(y))

    while x:

        if y:
            res = my_dict[x.pop()] + my_dict[y.pop()] + numeric
            #print(res)
            #print(numeric)

        else:
            res = my_dict[x.pop()] + numeric
           # print(res)
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


def multi_hex(x, y):
    my_dict = {a: str(a) for a in range(10)}
    my_dict.update({str(a): a for a in range(10)})
    my_dict.update({'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'})
    result = deque()
    spam = deque([deque() for _ in range(len(y))])
   # print(spam)

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



#num1 = list('A2')
#num2 = list('C4F')
num1 = list(input('Введите 1-е число: ').upper())
num2 = list(input('Введите 2-е число: ').upper())

print(*num1, '+', *num2, '= ', *summ_hex(num1, num2))

print(*num1, '*', *num2, '=', *multi_hex(num1, num2))