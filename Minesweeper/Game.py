from Field import Field
from time import time
import pickle


class Game:
    field_size = []
    bomb_count = int()
    game_field = ()
    players_field = []
    turns = 0
    bomb_found = 0
    game_stopped = False
    player_name = str()
    start_time = int()
    finish_time = int()

    def __init__(self, name):
        self.player_name = name

    def start_game(self):
        while True:
            print('Здравствуйте, ', self.player_name, '!', sep='')
            print('Вы игрете в "Сапер"')
            print('Выберите уровень сложности:')
            print('Введите цифру слева от описания уровня')
            print('1) Новичок: поле 5х5 и 5 бомб')
            print('2) Любитель: поле 8х8 и 10 бомб')
            print('3) Профессионал: поле 16х30 и 99 бомб')
            print('4) Задать свои параметры поля и бомб')
            print('5) Загрузить сохраненную игру')
            print('Введите exit для того, чтобы завершить игру')
            pick = input()
            if pick in ['1', '2', '3', '4', '5', 'exit']:
                self.start_time = time()
                break
            else:
                'Неправильный ввод данных'
        if pick == '1':
            self.field_size = (5, 5)
            self.bomb_count = 5
        elif pick == '2':
            self.field_size = (8, 8)
            self.bomb_count = 10
        elif pick == '3':
            self.field_size = (16, 30)
            self.bomb_count = 99
        elif pick == '4':
            print('Введите размер поля через пробел')
            while True:
                size = input().split(' ')
                try:
                    if int(size[0]) > 3 and int(size[1]) > 3:
                        self.field_size.append(int(size[0]))
                        self.field_size.append(int(size[1]))
                        break
                except (ValueError, IndexError):
                    print('Неправильно введены данные. Введите размер число строк >3 и '
                          'число столбцов >3 через пробел')
            print('Введите количество бомб')
            while True:
                try:
                    bombs = int(input())
                    self.bomb_count = bombs
                    if bombs <= 0 or bombs >= self.field_size[0] * self.field_size[1]-9:
                        print('Неверное число бомб')
                        continue
                    break
                except ValueError:
                    print('Неправильно введены данные. Введите число бомб')
        elif pick == '5':
            self.load_game()
        while not self.game_stopped:
            print('Ваш ход')
            print('Выберите клетку и действие в формате x, y, "Action"')
            print('Введите save для того, чтобы сохранить игру')
            print('Введите exit для того, чтобы завершить игру')
            pick = input().split(' ')
            if pick[0] == 'exit':
                return
            if pick[0] == 'save':
                self.save_game()
                return
            try:
                if len(pick) == 2:
                    pick.append('Open')
                x, y, action = pick
                if action == 'o':
                    action = 'Open'
                elif action == 'f':
                    action = 'Flag'
                elif action == 'u':
                    action = 'Unflag'
                if action not in ['Open', 'Flag', 'Unflag']:
                    print('Неправильный ввод данных')
                    continue
                if int(x) < 0 or int(y) < 0:
                    print('Неправильный ввод данных')
                    continue
                if int(x) >= self.field_size[0] or int(y) >= self.field_size[1]:
                    print('Неправильный ввод данных, вы ввели клетку вне поля')
                    continue
                self.player_turn((int(x), int(y)), action)
            except ValueError:
                print('Неправильный ввод данных')
        print('Совершено ходов', self.turns)

    def player_turn(self, pick, action="Open"):
        '''
        ход игрока
        :param pick: кортеж из (X,Y, Action)
        Action: Flag, Unflag, Open
        :return:
        '''
        self.turns += 1
        x = pick[0]
        y = pick[1]
        if self.turns == 1:
            self.game_field = Field(self.field_size, self.bomb_count, (x, y))
            self.players_field = ['*'] * self.game_field.field_size[0]
            for i in range(self.game_field.field_size[0]):
                self.players_field[i] = ['*'] * self.game_field.field_size[1]
            if self.game_field.field[x][y] == 0:
                self.open_zero(x, y)
        else:
            if action == 'Open':
                if self.players_field[x][y] != '*' and self.players_field[x][y] != '!':
                    print('Нельзя открыть уже открытую клетку')
                    self.turns -= 1
                    return
                if self.game_field.field[x][y] == 0:
                    self.open_zero(x, y)
                self.players_field[x][y] = self.game_field.field[x][y]
                print('Вы открыли, (', x, ';', y, ')!', sep='')
            elif action == 'Flag':
                if self.players_field[x][y] == '*':
                    self.players_field[x][y] = '!'
                    print('Вы поставили флаг в точку, (', x, ';', y, ')!', sep='')
                    if self.game_field.field[x][y] == -1:
                        self.bomb_found += 1
                else:
                    print('Нельзя поставить флаг на уже открытую ячейку')
                    self.turns -= 1
            elif action == 'Unflag':
                if self.players_field[x][y] == '!':
                    self.players_field[x][y] = '*'
                    print('Вы убрали флаг из точки, (', x, ';', y, ')!', sep='')
                    if self.game_field.field[x][y] == -1:
                        self.bomb_found -= 1
                else:
                    print('Флаг в точке(', x, ';', y, ') не был установлен!', sep='')
                    self.turns -= 1
        self.check_res(x, y, action)

    def open_zero(self, x, y):
        for i in (x, x-1, x+1):
            for j in (y, y-1, y + 1):
                if i != -1 and j != -1:
                    try:
                        if self.game_field.field[i][j] == 0 and (self.players_field[i][j] == '*' or
                                                                 self.players_field[i][j] == '!'):
                            self.players_field[i][j] = self.game_field.field[i][j]
                            self.open_zero(i, j)
                        if self.game_field.field[i][j] != -1:
                            self.players_field[i][j] = self.game_field.field[i][j]
                    except IndexError:
                        pass

    def print_game(self):
        print('  \033[4m', end='')
        for i in range(self.field_size[1]):
            if i < 10:
                s = '  '
            else:
                s = ' '
            print('\033[4m', i, sep=s, end='\033[0m')
        print()
        i = 0
        for row in self.players_field:
            if i < 10:
                print(' ', end='')
            print(i, end='| ')
            i += 1
            for item in row:
                print(item, end='  ')
            print()

    def check_res(self, x, y, action):
        if self.game_field.field[x][y] == -1 and action == 'Open':
            print('Вы попали на бомбу!')
            print('Вы проиграли')
            self.game_field.print_field()
            self.game_stopped = True
        else:
            self.print_game()
        if self.bomb_found == self.bomb_count:
            self.finish_time = time()
            print('Поздравляем вы выиграли!')
            print('Игра окончена за', ((self.finish_time - self.start_time) * 10000 // 100) / 100, 'секунд')
            self.game_stopped = True
            self.game_field.print_field()

    def save_game(self):
        with open('saves.txt', 'wb') as outfile:
            savedict = [self.game_field, self.players_field, self.turns,
                        time() - self.start_time, self.players_field,
                        self.bomb_found, self.bomb_count]
            pickle.dump(savedict, outfile)

    def load_game(self):
        with open('saves.txt', 'rb') as infile:
            savedict = pickle.load(infile)
            self.game_field = savedict[0]
            self.players_field = savedict[1]
            self.turns = savedict[2]
            self.start_time = savedict[3]
            self.players_name = savedict[4]
            self.bomb_found = savedict[5]
            self.bomb_count = savedict[6]
            self.field_size.append(len(self.players_field))
            self.field_size.append(len(self.players_field[0]))
        self.print_game()

