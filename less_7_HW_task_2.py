'''
 Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
 заданный случайными числами на промежутке [0; 50).
 Выведите на экран исходный и отсортированный массивы.

'''
from random import random

arr = [round((random ()*50),2) for i in range(10)]
print(arr)
def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:] + right[j:]
    return result


def merge_sort(left):
    if len(left) <= 1:
        return left
    else:
        l = left[:len(left) // 2]
        r = left[len(left) // 2:]
    return merge(merge_sort(l), merge_sort(r))


print(merge_sort(arr))

