#Author: Shyi
#-----------------------------------------------------------------------------------------------------------------------
# exercise 1
# from time import sleep
# class trafficlight:
#     __color = ['красный','желтый','зеленый']
#
#     def running(trafficlight):
#         i = 0
#         while True:
#             print(f'{trafficlight.__color[i]}')
#             if i % 3 == 0:
#                 sleep(2)
#             elif i % 3 == 2:
#                 sleep(11)
#             else:
#                 sleep(7)
#             if i > 1:
#                 i = 0
#                 print('Цикр цветов прошел')
#             else:
#                 i +=1
#
# trafficlight = trafficlight()
# trafficlight.running()
#-----------------------------------------------------------------------------------------------------------------------
# exercise 2
# class Road():
#     def __init__(self,_length, _width):
#         self.length = _length
#         self.width = _width
#
#     def massroad(self,length, width):
#         weidth = 25
#         depth = 5
#         weight = (self.length * self.width * weidth * depth)/1000
#         print(f'Масса асвальта необходимая для покрытия = {weight} т')
#
# l = int(input('Ввите длину'))
# w = int(input('введите ширину'))
#
# r = Road(l,w)
# r.massroad()

#-----------------------------------------------------------------------------------------------------------------------
# exercise 3
# class worker():
#     def __init__(self,p_surname, p_name, p_position, _income):
#         self.surname = p_surname
#         self.name = p_name
#         self.position = p_position
#         self.income = _income
#
# class position(worker):
#     def get_full_name(self):
#         print(f'Полное имя сотрудника - {self.surname} {self.name}')
#
#     def get_total_income(self):
#         sal = int(self.income.get('wage')) + int(self.income.get('premiums'))
#         print(f'Доход - ' + str(sal))
#
# w = position('Кузнецов', 'Кирилл', 'Инженер-програмист 2й категории', {'wage':'75000','premiums': '25000'})
#
# w.get_full_name()
# w.get_total_income()
#-----------------------------------------------------------------------------------------------------------------------
# exercise 4
from _ast import Is
# class Car:
#
#     def __init__(self,p_speed,p_color,p_name,p_is_police = False):
#         self.speed = p_speed
#         self.color = p_color
#         self.name = p_name
#         self.is_police = False
#
#     def go(self):
#         print(f'{self.color} {self.name} начал движение' )
#
#     def stop(self):
#         print(f'{self.color} {self.name} прекратил движение' )
#
#     def turn(self, direction):
#         print(f'{self.color} {self.name} повернул на {direction}' )
#
#     def show_speed(self):
#         print(f'{self.color} {self.name} движется со скоростью {self.speed}' )
#
# class TownCar(Car):
#     def __init__(self, *args, **knowards):
#         super().__init__(*args, **knowards)
#
#     def show_speed(self):
#         if self.speed > 60:
#             print(f'{self.color} {self.name} привысил скорость на {self.speed - 60} км/ч')
#         else:
#             print(Car.show_speed(self))
#
# class SportCar(Car):
#     def __init__(self, *args, **knowards):
#         super().__init__(*args, **knowards)
#
# class WorkCar(Car):
#     def __init__(self, *args, **knowards):
#         super().__init__(*args, **knowards)
#
#     def show_speed(self):
#         if self.speed > 40:
#             return f'{self.color} {self.name} привысил скорость на {self.speed - 40} км/'
#         else:
#             return Car.show_speed(self)
#
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police = True):
#         super().__init__(speed, color, name, is_police)
#         print(f'Это полицейская машина')
#
# sport = SportCar(120, 'Красный', 'Порше')
# sport.turn('left')
# sport.show_speed()
# 
# town = TownCar(70, 'Черный', 'БМВ')
# town.go()
# town.show_speed()
#
# work = WorkCar(100,'белый','Фольксваген')
# work.turn('направо')
# work.show_speed()
#
# police = PoliceCar('150', 'белый', 'Форд')
# police.go()
#-----------------------------------------------------------------------------------------------------------------------
# exercise 5
# class Stationery:
#     def __init__(self, title):
#         self.title = title
#
#     def draw(self):
#         print(f'канцелярия')
#
# class Pen(Stationery):
#     def draw(self):
#         print(f'{self.title}')
#
# class Pencil(Stationery):
#     def draw(self):
#         print(f'{self.title}')
#
# class Handle(Stationery):
#     def draw(self):
#         print( f'{self.title}')
#
# pen = Pen('ручка')
# pen.draw()
#
# pencil = Pencil('карандаш')
# pencil.draw()
#
# handle = Handle('фломастер')
# handle.draw()








