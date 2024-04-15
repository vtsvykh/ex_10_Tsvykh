import random


class NavalBattle:
    """
    Class of Naval battle.

    Attributes:
        playing_field : a 10х10 playing field
        symbol (str): the symbol that indicates the hit of each player
        type_ship (list): list of all ships
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
            print('игровое поле не заполнено')
        elif NavalBattle.playing_field[y - 1][x - 1] in (self.symbol, 'o'):
            print('ошибка')
        else:
            if NavalBattle.playing_field[y - 1][x - 1] == 1:
                NavalBattle.playing_field[y - 1][x - 1] = self.symbol
                print('попал')
            else:
                NavalBattle.playing_field[y - 1][x - 1] = 'o'
                print('мимо')

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
        Function places ships randomly on the playing field.
        :return: list of rosters with ships deployed
        """

        cls.playing_field = [['~'] * 10 for _ in range(10)]

        def is_valid_placement(x, y, ship_size, orientation):
            """
            Checks that the ship is correctly positioned at the specified location
            :param x: x coordinate
            :param y: y coordinate
            :param ship_size: size of the ship to be deployed
            :param orientation: orientation (vertical or horizontal)
            :return: True - the placement is correct, otherwise False.
            """
            for cage in range(ship_size):
                if orientation == 'horizontal':
                    if y + cage >= 10 or cls.playing_field[x][y + cage] != '~':
                        return False
                else:
                    if x + cage >= 10 or cls.playing_field[x + cage][y] != '~':
                        return False
            return True

        def mark_empty_cells(x, y):
            """
            The function surrounds the ship with empty cells
            :param x: coordinate x
            :param y: coordinate y
            :return: update playing field
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
                    for cage in range(ship_size):
                        if orientation == 'horizontal':
                            cls.playing_field[x][y + cage] = 1
                            mark_empty_cells(x, y + cage)
                        else:
                            cls.playing_field[x + cage][y] = 1
                            mark_empty_cells(x + cage, y)
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
