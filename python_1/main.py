#made by Shyi
#----------------------------task number 1
var1 = 0
var2 = 0.1
var3 = "0"

print("First var", type(var1), var1)
print("Second var", type(var2), var2)
print("Third var", type(var3), var3)

input1 = input("Fisrt var: ")
input2 = input("Second var: ")
input3 = input("Third var: ")

print("First var -> ", input1," Second var -> ", input2, " Third var -> ",input3)
#----------------------------task number 3
a = input("Enter n: ")
if a.isdigit():
    s = str(a) + str(a)
    t = str(a) + str(a) + str(a)
    a = int(a) + int(s) + int(t)
print(a)
#----------------------------task number 4
s = input("Enter the number -> ")
l = len(s)
i = 0
element = 0
if l > 0:
    while i < l:
        if s.isdigit(): # проверка строки на предмет символов
            if int(element) < int(s[i]):
                element = int(s[i])
            i = i + 1
        else:
            print("the variable must be a numeric type")
    print(element)
else:
    print("number must be more than 0")
#----------------------------task number 5
proceeds = input("proceeds -> ")
costs = input("costs -> ")

proceeds = int(proceeds)
costs = int(costs)

if proceeds < costs:
    print("the company could not make money")

if proceeds == costs:
    print("the company went to zero")

if proceeds > costs:
    print("the company was able to make money")
    proceeds = proceeds/costs
    emp = input("Enter the number of employees -> ")
    emp = int(emp)
    salary = proceeds/emp
    print("the salary per employee =",salary)
#----------------------------task number 6
a = input("First result -> ")
b = input("target km -> ")

a = int(a)
b = int(b)
i = 1
while a < b:
    print(i,"-й день: ",a)
    a = a + a * 0.1
    i = i + 1
print(i,"-й день: ",a)

print("Ответ: на", i, "-й день спортсмен достиг результата - не менее", b,"км.")