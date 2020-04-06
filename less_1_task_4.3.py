
'''
Допилил код = сейчас поиск случайного символа в заданных
границах не уходит в ноль...  соответственно
не дает ошибку. 
'''

from random import random, randint

c1 = ord(input(': '))
c2 = ord(input(': '))
print(c1, c2)
if c1<c2:
    c1,c2 = c2,c1
print (c1,c2)
m = randint(abs(c2),abs(c1))
print(chr(m))

