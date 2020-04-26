'''
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

'''
'''
В соответствии с заданием = взял исходную задачу и "засунул" в функцию, с генерацией случайного массива
в заданном диапазоне -100/100
представлено два варианта
с циклом for  и while
Есть понимание что улучшить не получилось...другой вопрос = на сколько получилось ухудшить??))

'''
li = [5,2,7,4,0,9,8,6]
n = 1
while n < len(li):
     for i in range(len(li)-n):
          if li[i] < li[i+1]:
               li[i],li[i+1] = li[i+1],li[i]
     n += 1
     print(li)
print(li)

# Решение:
from random import randint
from random import random


def gaz_air(arr):
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)


# li = [int(random ()*10) for i in range(10)]
li = [randint(-100, 100) for i in range(10)]
gaz_air(li)
print(li)


def gaz_air(arr):
    i = 0
    while i < len(li) - 1:
        j = 0
        while j < len(li) - 1 - i:
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
            j += 1
        i += 1
        print(li)


# li = [int(random ()*10) for i in range(10)]
li = [randint(-100, 100) for i in range(10)]
print(li)
gaz_air(li)
print(li)
