#Author: Shyi 12.09.2020
#Извините за то что здаю задание сейчас, был в командировке.
#exersice 1
my_box = ['list of items', 1 , 10000, '1', {'1': 'one', '2': 'two'}]
for item in my_box:
       print(type(my_box) ,my_box)
#exersice 2
user_box = []
i = 1
k = int(input('введите колличество элементов \n'))
while i <= k:
       print('введите',i,'значение')
       user_box.append(input())
       i += 1
print('ваше введенное значение ->', user_box)
user_box_length = len(user_box)
print('длина строки->',user_box_length)

if user_box_length % 2 != 0:
       user_box_length -= 1

i = 0
while i < user_box_length:
       user_box[i], user_box[i+1] = user_box[i+1], user_box[i]
       i += 2
print(user_box)
#exersice 3
seasons = ['зима','зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
mn = int(input('введите числовой эквивалент месяца \n'))
print('месяц ->', seasons[mn])
#exersice 4
user_in = input('Введите строку: \n')
user_in = user_in.split()
i = 1
for user_sw in user_in:
        print('{}, {:}'.format(i, user_sw[:10]))
        i += 1
#exersice 5
my_box = [7 ,5, 3, 3, 2]
user_inp = int(input('Введите натуральное числов: '))

if user_inp in my_box:
        idx_user_id = my_box.index(user_inp)
        my_box.insert(idx_user_id+1, user_inp)
elif user_inp < my_box[-1]:
        my_box.append(user_inp)
else:
        for num in my_box:
                if user_inp > num:
                        idx_user_id = my_box.index(num)
                        my_box.insert(idx_user_id, user_inp)
                        break
print(my_box)