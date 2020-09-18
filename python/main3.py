#Author Shyi
#--------------------------------------------------------------------------------------------------
#exersice 1
def division(numer, denom):
    if denom == 0:
        return 'Деление на 0 запрещенно'
    return numer / denom
user_in = int(input('Введите числитель: ')), int(input('Введите знаминатель: '))
print(division(*user_in))
print(type(user_in))
#--------------------------------------------------------------------------------------------------
#exersice 2
def show_data(*,surname, name, patron, birth, birth_place, email, phone):
    print(f'ФИО: {surname}, {name}, {patron}, Дата Рождения: {birth}, '
          f'Место Рождения: {birth_place}, email: {email}, Номер телефона: {phone}')
surname_in = input('Фамилию: ')
name_in = input('Имя: ')
patron_in = input('Отчество: ')
birth_in = input('Дату рождения: ')
birth_place_in = input('Место Рождения: ')
email_in = input('email: ')
phone_in = input('Номер телефона: \n')

show_data(surname = surname_in
        , name = name_in
        , patron = patron_in
        , birth = birth_in
        , birth_place = birth_place_in
        , email = email_in
        , phone = phone_in)
#--------------------------------------------------------------------------------------------------
#exersice 3
def fun(*args):
    arguments = sorted(args)
    max_arg = arguments[1:]
    return max_arg[0] + max_arg[1]
print(fun(20,40,50))
#exersice 4
def fun(x, y):
    return x ** y
user_in1 = float(input('Введите действительное положительное число:'))
user_in2 = int(input('Введите отрицательное целое число:'))
print(fun(user_in1, user_in2))
#--------------------------------------------------------------------------------------------------
#exersice 5
def sum():
    result = 0
    while 1 == 1:
        user_data = input('Введите целые числа через пробел, либо напишите "end" \n')
        for number in user_data.split():
            if number =='end':
                return result
            result += int(number)
        print('Значение = ', result)
    return result

sum_n = sum()
print(sum_n)
#--------------------------------------------------------------------------------------------------
#exersice 6
def fun(user_in):
    txt_in = user_in.split()
    txt_result = []
    for word in txt_in:
        txt_result.append(word.capitalize())
    return ' '.join(txt_result)
user_txt_in = input('введети текст из маленьких латинских букв разделенные пробелом.')
print(fun(user_txt_in))