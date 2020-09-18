#Author: Shyi
#exercise 1
# f = open('C:/file1.txt', 'w')
# while True:
#     user_ans = input('Введите строку'+ '\n')
#     if user_ans == '' :
#         f.close()
#         break
#     f.write(user_ans + '\n')
# print(f)
#-----------------------------------------------------------------------------------------------------------------------
#exercise 2
# f = open('C:/file1.txt')
# line = 0
# for i in f:
#     line += 1
#
#     flag = 0
#     word = 0
#     for j in i:
#         if j != ' ' and flag == 0:
#             word += 1
#             flag = 1
#         elif j == ' ':
#             flag = 0
#
#     print('стр. №',line,',', len(i), 'симв.', word, 'сл.')
#
# print(line, 'стр.')
# f.close()
#-----------------------------------------------------------------------------------------------------------------------
#exercise 3
# f = open('C:/file1.txt', encoding='UTF-8')
# sum = 0
# count = 0
# for line in f:
#     surname, sal = line.split()
#     sum += int(sal)
#     count += 1
#     if int(sal) < 20000:
#         print(surname, sal)
# print('avarage sal: ', sum / count)
# f.close()
#-----------------------------------------------------------------------------------------------------------------------
#exercise 4
# num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять'}
# f = open('C:/file1.txt')
# f2 = open('C:/file2.txt')
# ln = [line.split() for line in f]
# nln = [[num[elem[0]], elem[1],elem[2]] for elem in ln]
# for elem in nln:
#     f2.writelines(''.join(elem) + '\n')
#-----------------------------------------------------------------------------------------------------------------------
#exercise 5
# import random
#
# f = open('C:/file1.txt', 'w+')
# i = 0
# while i < 100:
#     i += 1
#     num = random.randint(0,100)
#     f.write(str(num) + ' ')
# f.close()
#
# f = open('C:/file1.txt', 'r')
# tt = [int(elem) for elem in f.read().split()]
# print('Sum = ', sum(tt))
# f.close()
#-----------------------------------------------------------------------------------------------------------------------
#exerсise 6
f = open('C:/file1.txt')
box = {}
for line in f:
    h = line.split()
    for i in range(1,4):
        if h[i] != '-':
            h[i] = int(h[i].rstrip('лпраб'))
        else:
            h[i] = 0
    box[h[i].rstrip(':')] = sum(h[1:])
print(box)


