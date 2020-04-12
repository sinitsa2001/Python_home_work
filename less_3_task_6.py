'''

6.	В одномерном массиве найти сумму элементов, находящихся между
минимальным и максимальным элементами. Сами минимальный и максимальный
элементы в сумму не включать.
'''

from random import random

SIZE = 10
arr = [0] * SIZE
for i in range(SIZE):
    arr[i] = int(random() * 100)
    print(arr[i], end=' ')
print()

min_el = 0
max_el = 0
for i in range(1, SIZE):
    if arr[i] < arr[min_el]:
        min_el = i
    elif arr[i] > arr[max_el]:
        max_el = i
print(arr[min_el], arr[max_el])

if min_el > max_el:
    min_el, max_el = max_el, min_el

res_sum = 0
for i in range(min_el + 1, max_el):
    res_sum += arr[i]
print(res_sum)
