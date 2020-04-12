
'''
3.	В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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
for i in range(SIZE):
    if arr[i] < arr[min_el]:
        min_el = i
    elif arr[i] > arr[max_el]:
        max_el = i
spam = arr[min_el]
arr[min_el] = arr[max_el]
arr[max_el] = spam

for i in range(SIZE):
    print(arr[i], end=' ')
print()
