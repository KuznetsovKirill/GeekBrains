#Author: Shyi
#первое задание работает не верно, сделал сам, потом открыл Ваш пример, как вы сделали, все равно не работает, выдает ошибку
#если обращаюсь как было у вас в уроке, то выдает с индексом ошибку
#(<class 'IndexError'>, IndexError('list index out of range'), <traceback object at 0x046DCC68>)
#если обращаюсь
#(<class 'ValueError'>, ValueError('not enough values to unpack (expected 4, got 1)'), <traceback object at 0x041DDC88>)
#exersice 1
import sys
def fun_salary (hours, per_hour=1, prize=5000):
    salary = int(hours) * int(per_hour) + int(prize)
    return salary
# script_name = int(sys.argv[1])
# hours = sys.argv[2]
# per_hour = int(sys.argv[3])
# prize = int(sys.argv[4])
script_name, hours, per_hour, prize = sys.argv
print(f' Ваша заработная плата за этот месяц: {fun_salary(hours,per_hour,prize=prize)}')
#-----------------------------------------------------------------------------------------------------------------------
#exersice 2
my_box = [1, 2, 3, 1, 154, 488, 12, 10, 77, 2, 78, 1234, 5555]
i = 1
res = [my_box[num]
       for num in range(i,len(my_box))
       if my_box[num] > my_box[num-1]]
print(res)
#-----------------------------------------------------------------------------------------------------------------------
#exersice 3
from random import randrange
print([elem for elem in [randrange(20,241) for i in range(30)] if ((elem % 20 == 0) or (elem % 21 == 0))])
#-----------------------------------------------------------------------------------------------------------------------
#exersice 4
my_box = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([elem for elem in my_box if my_box.count(elem) == 1])
#-----------------------------------------------------------------------------------------------------------------------
#exersice 5
from functools import reduce

def fun(elem, prev):
    return elem * prev
my_box = [elem for elem in range(100,1001) if elem % 2 == 0]
print(reduce(fun,my_box))
#-----------------------------------------------------------------------------------------------------------------------
#exersice 6
# не получилось сделать
#-----------------------------------------------------------------------------------------------------------------------
#exersice 7
def fun(num):
    for n in range(num+1):
        res = 1
        for i in range(1, n+1):
            res *= i
        yield res
for num in fun(4):
    print(num)




