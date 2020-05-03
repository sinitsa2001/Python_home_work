'''
1.	Определить количество различных подстрок с использованием хеш-функции.
Задача: на вход функции дана строка, требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.

'''

'''
!!! Не уверен что получилось...поэтому специльно не убираю ход мыслей..
буду признателен за правки!!! 

'''
import hashlib


def subs_count(my_str):
    hash_set = set()
    my_my = set()

    for i in range(len(my_str)+1):

        for j in range(i + 1, len(my_str)+1):
            h1 =hashlib.sha1(my_str.encode('utf-8')).hexdigest()
            #print (f'h1{h1}')
            h = hashlib.sha1(my_str[i:j].encode('utf-8')).hexdigest()
            #print(f'h:{h}')
            hash_set.add(h)
            my_my.add(h1)
            #print(my_my)
            #if set(my_my).intersection(set(hash_set)):
             #print('yes')
            hash_set.discard(h1)
            #print(len(hash_set))



    return len(hash_set)


my_str = 'bsma'


print(f'Подстрок в строке "{my_str}": получилось: {subs_count(my_str)}')

