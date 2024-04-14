class NavalBattle:
    """
    Class of Naval battle.

    Attributes:
        playing_field (list): a list of lists denoting a 10х10 playing field
        symbol (str): the symbol that indicates the hit of each player
    """
    playing_field = [['~'] * 10 for _ in range(10)]

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
        if NavalBattle.playing_field[y - 1][x - 1] == 1:
            NavalBattle.playing_field[y - 1][x - 1] = self.symbol
            print("попал")
        else:
            NavalBattle.playing_field[y - 1][x - 1] = 'o'
            print("мимо")

    @staticmethod
    def show():
        """
        Displays the current playing field.
        """
        for i in range(10):
            for j in range(10):
                if NavalBattle.playing_field[i][j] == 0 or NavalBattle.playing_field[i][j] == 1:
                    print('~', end=' ')
                else:
                    print(NavalBattle.playing_field[i][j], end=' ')
            print()
        print('\n')

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
