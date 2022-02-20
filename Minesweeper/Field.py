import random

class Field:
    '''
    Класс Field описывает игровое поле
    -1 - в клетке бомба
    Инициализируется с параметрами размер поля и количество бомб
    '''
    field_size = []
    first_pick = []
    field = []
    bomb_count = int()

    def __init__(self, field_size, bomb_count, first_pick):
        self.field_size = field_size
        self.bomb_count = bomb_count
        self.first_pick = first_pick
        #заполняем поле нулями
        self.field = [0] * self.field_size[0]
        for i in range(self.field_size[0]):
            self.field[i] = [0] * self.field_size[1]
        #заполняем поле бомбами
        bomb_counter = 0
        while bomb_counter != self.bomb_count:
            a = random.randint(0, self.field_size[0]-1)
            b = random.randint(0, self.field_size[1]-1)
            if self.field[a][b] != 0 or (self.first_pick[0]-1 <= a <= self.first_pick[0]+1 and
                                         self.first_pick[1]-1 <= b <= self.first_pick[1]+1):
                pass
            else:
                self.field[a][b] = -1
                bomb_counter += 1
        #заполним поле цифрами
        for i in range(self.field_size[0]):
            for j in range(self.field_size[1]):
                bombs_sum = 0
                if self.field[i][j] != -1:
                    for i1 in range(i - 1, i + 2):
                        for j1 in range(j - 1, j + 2):
                            try:
                                if self.field[i1][j1] == -1 and i1 != -1 and j1 != -1:
                                    bombs_sum += 1
                            except IndexError:
                                pass
                    self.field[i][j] = bombs_sum

    def print_field(self):
        print('   \033[4m', end='')
        for i in range(self.field_size[1]):
            if i < 10:
                s = '  '
            else:
                s = ' '
            print('\033[4m', i, sep=s, end='\033[0m')
        print()
        # print('_' * 12)
        i = 0
        for row in self.field:
            if i < 10:
                print(' ', end='')
            print(i, end='| ')
            i += 1
            for item in row:
                if item != -1:
                    print(' ', end='')
                print(item, end=' ')
            print()
