#Author: Shyi
#-----------------------------------------------------------------------------------------------------------------------
#exercise 1
class Matrix:
    @staticmethod
    def check_list(lst):
        ln = [len(el) for el in lst]
        return True if len(set(ln)) <= 1 else False

    def __init__(self, elem_list):
        if not Matrix.check_list(elem_list):
            raise Exception('Не возможно преобразовать в матрицу')
        self.__matrix = elem_list

    def __str__(self):
        matrix_str =''
        for line in self.__matrix:
            for el in line:
                matrix_str = matrix_str + '\t' + str(el)
            matrix_str = matrix_str + '\n'
        return matrix_str

    def __add__(self, other):
        if type(other) is not Matrix:
            raise Exception('Недопустимый тип слагаемого')
        res_mat =[]
        for line1,line2 in zip(self.__matrix, other.__matrix):
            new_line = [a + b for a,b in zip(line1,line2)]
            res_mat.append(new_line)
        return Matrix(res_mat)
test_list  = [[1,2,3], [4,5,6], [1,4,6], [6,4,8]]
test_list2 = [[6,9,8], [4,7,8], [3,2,1], [5,4,3]]
test = Matrix(test_list)
print(test)
test2 = Matrix(test_list2)
print(test2)
res = test + test2
print('Сумма матриц:\n', res)
#-----------------------------------------------------------------------------------------------------------------------
#exercise 2
from abc import ABC, abstractmethod

class Habliment(ABC):
    def __init__(self, value):
        self.__name = value

    @property
    def name(self):
        return self.__name

    @abstractmethod
    def fabric_consumption(self):
        pass

class Coat(Habliment):
    def __init__(self, name, size):
        super().__init__(name)
        self.__size = size

    def fabric_consumption(self):
        return self.__size / 6.5 + 0.5

class Costume(Habliment):
    def __init__(self, name, height):
        super().__init__(name)
        self.__height = height

    def fabric_consumption(self):
            return self.__height * 2 + 0.3

def print_consuption(hab):
    print(f'Расход ткани на {hab.name} равено {hab.fabric_consumption()}')

c = Coat('пальто', 50)
d = Costume('костюм', 150)
print_consuption(c)
print_consuption(d)
print('Расход ткани общий - ', c.fabric_consumption() + d.fabric_consumption())
#-----------------------------------------------------------------------------------------------------------------------
#exercise 3
class Cell:
    def __init__(self, alveolus):
        if type(alveolus) is not int:
            raise ValueError
        if alveolus <=0:
            raise ValueError('Кол-во ячеек в клетке должно быть больше 0')
        self.alveolus_count = alveolus

    def __add__(self, other):
        if type(other) is not Cell:
            raise ValueError

        return Cell(self.alveolus_count + other.alveolus_count)

    def __mul__(self, other):
        if type(other) is not Cell:
            raise ValueError

        return Cell(self.alveolus_count * other.alveolus_count)

    def __truediv__(self, other):
        if type(other) is not Cell:
            raise ValueError
        new_all_count = self.alveolus_count // other.alveolus_count
        if new_all_count == 0:
            raise ValueError('В результате деления - ячеек не соталось')
        return Cell(new_all_count)

    def __sub__(self, other):
        if type(other) is not Cell:
            raise ValueError
        new_all_count = self.alveolus_count - other.alveolus_count
        if new_all_count == 0:
            raise ValueError('В результате вычитания - ячеек не соталось')
        return Cell(new_all_count)

    def make_order(self, row):
        num = self.alveolus_count
        res = ''
        while num > row:
            res = res + '*' * row + '\n'
            num -= row
        res = res + '*' * num
        return res

c = Cell(20)
print(c.make_order(30))
d = Cell(70)
print(d.make_order(4))
k = Cell(11)
a = d - c + k
print(a.make_order(5))
print(a.alveolus_count)
a = d * c
print(a.alveolus_count)
a = a / k
print(a.alveolus_count)

