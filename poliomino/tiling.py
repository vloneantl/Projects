class Field:
    def __init__(self, field_size):
        self.field_size = field_size
        self.field = []
        for i in range(self.field_size[0]):
            self.field.append([0] * self.field_size[1])

    def check_square(self, list_of_poliomino):
        '''
        метод проверяет возможность замощения, исходя из площади заданных полиомино
        если площадь всех полиомионо < площади поля, метод возвращает False
        '''
        sumpr = 0
        for poliomino in list_of_poliomino:
            #проверка на условие по площади
            if poliomino.type == 0:
                pr = poliomino.size[0] * poliomino.size[1]
            else:
                pr = poliomino.size[0] + poliomino.size[1] - 1
            sumpr += pr
        if sumpr > self.field_size[0] * self.field_size[1]:
            print('не выполняется условие по площади')

    def print_field(self):
        for i in range(self.field_size[0]):
            print(self.field[i])

    def check_possibility(self, type, size, point):
        #проверяет возможность размещения фигуры в заданной клетке point
        if type == 0:
            for i in range(size[0]):
                for j in range(size[1]):
                    if point[0] + i >= self.field_size[0]:
                        return False
                    if point[1] + j >= self.field_size[1]:
                        return False
                    if self.field[point[0] + i][point[1] + j] != 0:
                        return False
            return True
        if type == 1:
            for i in range(size[0]):
                if point[0] + i >= self.field_size[0]:
                    return False
                if self.field[point[0] + i][point[1]] != 0:
                    return False
            for j in range(size[1]):
                if point[1] + j >= self.field_size[1]:
                    return False
                if self.field[point[0]][point[1] + j] != 0:
                    return False
        if type == 2:
            for j in range(size[0]):
                if point[1] + j >= self.field_size[1]:
                    return False
                if self.field[point[0]][point[1] + j] != 0:
                    return False
            for i in range(size[1]):
                if point[0] + i >= self.field_size[0]:
                    return False
                if self.field[point[0] + i][point[1] + size[0] - 1] != 0:
                    return False
        if type == 3:
            for j in range(size[1]):
                if point[1] - j < 0 or point[0] + size[0] - 1 >= self.field_size[0]:
                    return False
                if self.field[point[0] + size[0] - 1][point[1] - j] != 0:
                    return False
            for i in range(size[0]):
                if point[0] + i >= self.field_size[0]:
                    return False
                if self.field[point[0] + i][point[1]] != 0:
                    return False
        if type == 4:
            for i in range(size[1]):
                if point[0] + i >= self.field_size[0]:
                    return False
                if self.field[point[0] + i][point[1]] != 0:
                    return False
            for j in range(size[0]):
                if point[1] + j >= self.field_size[1]:
                    return False
                if self.field[point[0] + size[1] - 1][point[1] + j] != 0:
                    return False
        return True

    def place_poliomino(self, type, size, point, number):
        '''
        меняет значения в field для определения клеток, в которые нельзя
        разместить полиомино
        '''
        if type == 0:
            for i in range(size[0]):
                for j in range(size[1]):
                    self.field[point[0] + i][point[1] + j] = number
        if type == 1:
            for i in range(size[0]):
                self.field[point[0] + i][point[1]] = number
            for j in range(size[1]):
                self.field[point[0]][point[1] + j] = number
        if type == 2:
            for j in range(size[0]):
                self.field[point[0]][point[1] + j] = number
            for i in range(size[1]):
                self.field[point[0] + i][point[1] + size[0] - 1] = number
        if type == 3:
            for j in range(size[1]):
                self.field[point[0] + size[0] - 1][point[1] - j] = number
            for i in range(size[0]):
                self.field[point[0] + i][point[1]] = number
        if type == 4:
            for i in range(size[1]):
                self.field[point[0] + i][point[1]] = number
            for j in range(size[0]):
                self.field[point[0] + size[1] - 1][point[1] + j] = number

    def find_place(self, poliomino, number):
        '''
        ищет клетку в которую можно теоретически разместить полиомино
        возвращает True, если полиомино можно разместить, иначе False
        '''
        type = poliomino.type
        size = poliomino.size
        if type == 0:
            for i in range(self.field_size[0]):
                for j in range(self.field_size[1]):
                    point = (i, j)
                    if (point, size) in poliomino.banned_positions:
                        if (point, (size[1], size[0])) not in poliomino.banned_positions:
                            size = (size[1], size[0])
                            poliomino.size = size
                            if self.check_possibility(type, size, point):
                                self.place_poliomino(type, size, point, number)
                                poliomino.change_position(point)
                                poliomino.ban_position(point, size)
                                return True
                        continue
                    if self.field[i][j] == 0:
                        if self.check_possibility(type, size, point):
                            self.place_poliomino(type, size, point, number)
                            poliomino.change_position(point)
                            poliomino.ban_position(point, size)
                            return True
                        size = (size[1], size[0])
                        poliomino.size = size
                        if ((i, j), size) not in poliomino.banned_positions:
                            if self.check_possibility(type, size, point):
                                self.place_poliomino(type, size, point, number)
                                poliomino.change_position(point)
                                poliomino.ban_position(point, size)
                                return True
        if type in (1, 2, 3, 4):
            for i in range(self.field_size[0]):
                for j in range(self.field_size[1]):
                    point = (i, j)
                    if self.field[i][j] == 0:
                        for type in (1, 2, 3, 4):
                            if (point, type) not in poliomino.banned_positions:
                                if self.check_possibility(type, size, point):
                                    poliomino.type = type
                                    self.place_poliomino(type, size, point, number)
                                    poliomino.change_position(point)
                                    poliomino.ban_position(point, type)
                                    return True
        return False

    def drop_poliomino(self, poliomino):
        '''
        меняет значения в field, если нужно переместить полиомино
        '''
        type = poliomino.type
        size = poliomino.size
        point = poliomino.position
        if type == 0:
            for i in range(size[0]):
                for j in range(size[1]):
                    self.field[point[0] + i][point[1] + j] = 0
        if type == 1:
            for i in range(size[0]):
                self.field[point[0] + i][point[1]] = 0
            for j in range(size[1]):
                self.field[point[0]][point[1] + j] = 0
        if type == 2:
            for j in range(size[0]):
                self.field[point[0]][point[1] + j] = 0
            for i in range(size[1]):
                self.field[point[0] + i][point[1] + size[0] - 1] = 0
        if type == 3:
            for j in range(size[1]):
                self.field[point[0] + size[0] - 1][point[1] - j] = 0
            for i in range(size[0]):
                self.field[point[0] + i][point[1]] = 0
        if type == 4:
            for i in range(size[1]):
                self.field[point[0] + i][point[1]] = 0
            for j in range(size[0]):
                self.field[point[0] + size[1] - 1][point[1] + j] = 0


class Poliomino:
    def __init__(self, type, size):
        self.type = type
        self.size = size
        self.position = (-1, -1)
        self.banned_positions = set()

    def change_position(self, point):
        self.position = (point[0], point[1])

    def ban_position(self, point, size):
        self.banned_positions.add((point, size))


def tiling(field_size, rectangles, lpoliomino):
    field_size = field_size[1], field_size[0]
    field = Field(field_size)
    list_of_poliominos = []
    for poliomino in rectangles:
        for _ in range(poliomino[1]):
            obj = Poliomino(0, (poliomino[0][1], poliomino[0][0]))
            list_of_poliominos.append(obj)
    for poliomino in lpoliomino:
        for _ in range(poliomino[1]):
            obj = Poliomino(2, (poliomino[0][1], poliomino[0][0]))
            list_of_poliominos.append(obj)
    if field.check_square(list_of_poliominos) == False:
        return False
    k = 0
    while k != len(list_of_poliominos):
        if field.find_place(list_of_poliominos[k], k + 1):
            k += 1
        else:
            k -= 1
            if k == -1:
                print('Замощение невозможно')
                return False
            if k + 2 < len(list_of_poliominos):
                for i in range(k + 1, len(list_of_poliominos)):
                    list_of_poliominos[i].banned_positions = set()
            field.drop_poliomino(list_of_poliominos[k])
    print('Замощение возможно')
    field.print_field()
    return True


def menu():
    rectangles = []
    l_poliomino = []
    field_size = -1
    while True:
        print('Введите 1 для ввода информации о размере прямоугольника-стола')
        print('Введите 2 для ввода информации о прямоугольном полиомино')
        print('Введите 3 для ввода информации о L-полиомино')
        print('Введите 4 для вывода уже введенной информации')
        print('Введите 5 для запуска программы')
        print('Введите 6 для того, чтобы начать ввод данных заново')
        print('Введите 0 для выхода из программы')
        choise = int(input())
        if choise == 1:
            print('Введите размер поля через пробел')
            field_size = input()
            field_size = tuple(int(x) for x in field_size.split(" "))
        if choise == 2:
            print('Введите ширину и высоту прямоугольного полиомино через пробел')
            size = input()
            size = tuple(int(x) for x in size.split(" "))
            print('Введите количество таких полиомино')
            count = int(input())
            rectangles.append((size, count))
        if choise == 3:
            print('Введите параметры(длина левой и нижней "коемки") L-полиомино через пробел')
            size = input()
            size = tuple(int(x) for x in size.split(" "))
            print('Введите количество таких полиомино')
            count = int(input())
            l_poliomino.append((size, count))
        if choise == 4:
            print('Размер поля:')
            print(field_size)
            print('Прямоугольные полиомино:')
            for item in rectangles:
                print(item)
            print('L-полиомино:')
            for item in l_poliomino:
                print(item)
        if choise == 5:
            if field_size == -1:
                print('Введите размер поля')
                continue
            return tiling(field_size, rectangles, l_poliomino)
        if choise == 6:
            rectangles = []
            l_poliomino = []
        if choise == 0:
            return


menu()
