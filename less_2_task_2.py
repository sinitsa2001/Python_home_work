
'''
Например, если введено число 34560, в нем 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
'''

num = int(input('Введите натуральное число: '))
even_num = 0
odd_num = 0

while num > 0:
    if num % 2 == 0:
        even_num += 1
    else:
        odd_num += 1
    num = num // 10
print(f'Четные числа:{even_num}, Нечетные числа: {odd_num}')



num = int(input('Введите натуральное число: '))
even_num = 0
odd_num = 0


def even(n, s):
    if n <= 0:
        return s
    else:
        if n % 2 == 0:
            s += 1
        n = n //10

        return even(n, s)


def odd(n, s):
    if n <= 0:
        return s
    else:
        if not n % 2 == 0:
            s += 1
        n = n //10
        return odd(n, s)


print("Четные числа:%d" % (even(num, 0)))
print("Нечетные числа:%d" % (odd(num, 0)))
