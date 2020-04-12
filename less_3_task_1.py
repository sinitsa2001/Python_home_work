
'''
1.	В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''


arr = [0] * 8
# print(*a)
for x in range(2, 100):

    for y in range(2, 10):
        if x % y == 0:
            arr[y - 2] += 1
            # print(arr)
x = 0
while x < len(arr):
    res = x+2
    result = arr[x]
    x += 1
    print(res, '->>', result)
