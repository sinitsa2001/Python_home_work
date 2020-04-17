'''
Как говориться = тема не легла.
крутил вертел ничего не получил
урок смотрел = там все просто. начал "ковырять"  и стало все сложно
буду признателен за совет = где почитать = чтобы разобраться. ибо  это требуется

'''

import timeit
import cProfile


def fibo_gen(n):
    m = 1
    for i in range(1, n):
        if i == 26:
            break
        m *= i
        yield m
for i in fibo_gen(100):
 print(f' = {i}')

#print(fibo_gen(10))

print(timeit.timeit('fibo_gen(10)', number=10, globals=globals()))#0.00014668300000000162
print(timeit.timeit('fibo_gen(100)', number=10, globals=globals()))#1.4873999999998055e-05
print(timeit.timeit('fibo_gen(1000)', number=10, globals=globals()))#1.5722000000002734e-05
print(timeit.timeit('fibo_gen(10000)', number=10, globals=globals()))#1.2797999999994425e-05
print(timeit.timeit('fibo_gen(100000)', number=10, globals=globals()))#1.1226999999995602e-05

print(timeit.timeit('fibo_gen(100)', number=10, globals=globals()))#9.383000000001696e-06
print(timeit.timeit('fibo_gen(100)', number=100, globals=globals()))#7.166100000000064e-05
print(timeit.timeit('fibo_gen(100)', number=1000, globals=globals()))#0.0007132710000000014
print(timeit.timeit('fibo_gen(100)', number=10000, globals=globals()))#0.0037843169999999954
print(timeit.timeit('fibo_gen(100)', number=100000, globals=globals()))#0.038503908

cProfile.run('fibo_gen(10)')
cProfile.run('fibo_gen(100)')
cProfile.run('fibo_gen(1000)')
cProfile.run('fibo_gen(10000)')
cProfile.run('fibo_gen(100000)')
cProfile.run('fibo_gen(1000000000)')


from itertools import count
from math import factorial


def fibo_gen():
    for el in count(1):
        yield factorial(el)

generator = fibo_gen()
x = 0
for i in generator:
    if x == 25:
        break
    else:
        x += 1
        print(f"Factorial {x} = {i}")
#print(fibo_gen())


print(timeit.timeit('fibo_gen()', number=10, globals=globals()))#1.132800000000489e-05
print(timeit.timeit('fibo_gen()', number=100, globals=globals()))#6.497399999999542e-05
print(timeit.timeit('fibo_gen()', number=1000, globals=globals()))#0.0006079220000000107
print(timeit.timeit('fibo_gen()', number=10000, globals=globals()))#0.003720647999999993
print(timeit.timeit('fibo_gen()', number=100000, globals=globals()))#0.05396906500000001

cProfile.run('fibo_gen()')
