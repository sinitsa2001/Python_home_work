
'''
9.	Среди натуральных чисел, которые были введены,
найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
'''
'''
!!! Задача НЕ доделана.Сломались мозги. 
По факту - удалось посчитать цифр в числе...но не хватает разума(пока) - 
а) закинуть это в круговорот
б) сделать так чтобы все введенные и посчитанные значения запомнились...и сравнились между собой
..будем искать. 
пока сдаю в таком виде...если успею до дедлайна - перезакину файл в репозиторий

'''

a1 = int(input("Введите целое число: "))
#a2 = int(input('Введите другое число: '))

def func(n):
    b = 0
    while n > 0:
        num = n % 10
        b = b + num
        n = n // 10
    print(b)
func(a1)
#func(a2)