import random


class NavalBattle:
    """
    Class of Naval battle.

    Attributes:
        playing_field (list): a list of lists denoting a 10х10 playing field
        symbol (str): the symbol that indicates the hit of each player
    """
    playing_field = None
    type_ship = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    def __init__(self, symbol):
        """
        The function initializes a new class object.
        :param symbol: the symbol that indicates the hit of each player
        """
        self.symbol = symbol

    def shot(self, x, y):
        """
        Allows player to make a move at the specified coordinates, returns the result of the move: "Попал!" or "Мимо!".
        :param x: the value of the x coordinate
        :param y: the value of the y coordinate
        :return: the result of the execution of the move
        """

        if NavalBattle.playing_field == None:
            print('Игровое поле не заполнено!')
        elif NavalBattle.playing_field[y - 1][x - 1] in (self.symbol, 'o'):
            print('Ошибка!')
        else:
            if NavalBattle.playing_field[y - 1][x - 1] == 1:
                NavalBattle.playing_field[y - 1][x - 1] = self.symbol
                print('Попал!')
            else:
                NavalBattle.playing_field[y - 1][x - 1] = 'o'
                print('Мимо!')

    @staticmethod
    def show():
        """
        Displays the current playing field.
        """
        for i in range(10):
            for j in range(10):
                if NavalBattle.playing_field[i][j] in (1, 0, ' '):
                    print('~', end=' ')
                else:
                    print(NavalBattle.playing_field[i][j], end=' ')
            print()
        print()

    @classmethod
    def new_game(cls):
        """
        Расставляет корабли случайным образом на доске.

        Args:
            board_size (int): Размер доски (например, 10 для 10x10).
            ship_sizes (list): Список размеров кораблей (например, [5, 4, 3, 3, 2]).

        Returns:
            list: Двумерный список, представляющий доску с кораблями.
        """
        cls.playing_field = [['~'] * 10 for _ in range(10)]

        def is_valid_placement(y, x, ship_size, orientation):
            """
            Проверяет, что корабль может быть размещен в данной позиции.

            Args:
                x (int): Координата X.
                y (int): Координата Y.
                ship_size (int): Размер корабля.
                orientation (str): Ориентация ('horizontal' или 'vertical').

            Returns:
                bool: True, если размещение корректно, иначе False.
            """
            for i in range(ship_size):
                if orientation == 'horizontal':
                    if y + i >= 10 or cls.playing_field[x][y + i] != '~':
                        return False
                else:
                    if x + i >= 10 or cls.playing_field[x + i][y] != '~':
                        return False
            return True

        def mark_empty_cells(x, y):
            """
            Окружает корабль пустыми клетками.

            Args:
                x (int): Координата X.
                y (int): Координата Y.
            """
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < 10 and 0 <= new_y < 10:
                        if cls.playing_field[new_x][new_y] == '~':
                            cls.playing_field[new_x][new_y] = ' '

        for ship_size in NavalBattle.type_ship:
            placed = False
            while not placed:
                orientation = random.choice(['horizontal', 'vertical'])
                if orientation == 'horizontal':
                    x = random.randint(0, 10 - 1)
                    y = random.randint(0, 10 - ship_size)
                else:
                    x = random.randint(0, 10 - ship_size)
                    y = random.randint(0, 10 - 1)

                if is_valid_placement(y, x, ship_size, orientation):
                    for i in range(ship_size):
                        if orientation == 'horizontal':
                            cls.playing_field[x][y + i] = 1
                            mark_empty_cells(x, y + i)
                        else:
                            cls.playing_field[x + i][y] = 1
                            mark_empty_cells(x + i, y)
                    placed = True

        return cls.playing_field

    def __str__(self):
        """
        Displaying information about a class object to users.
        """
        return (f'Символ игрока: {self.symbol}\n'
                f'Текущее игровое поле: {NavalBattle.playing_field}')

    def __repr__(self):
        """
        Displaying information about a class object in debugging mode.
        """
        return f'{NavalBattle.playing_field}'

