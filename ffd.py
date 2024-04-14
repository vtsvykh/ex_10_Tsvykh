import random


def place_ships(board_size, ship_sizes):
    """
    Расставляет корабли случайным образом на доске.

    Args:
        board_size (int): Размер доски (например, 10 для 10x10).
        ship_sizes (list): Список размеров кораблей (например, [5, 4, 3, 3, 2]).

    Returns:
        list: Двумерный список, представляющий доску с кораблями.
    """
    board = [['~'] * board_size for _ in range(board_size)]

    def is_valid_placement(x, y, ship_size, orientation):
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
                if y + i >= board_size or board[x][y + i] != '~':
                    return False
            else:
                if x + i >= board_size or board[x + i][y] != '~':
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
                if 0 <= new_x < board_size and 0 <= new_y < board_size:
                    if board[new_x][new_y] == '~':
                        board[new_x][new_y] = ' '

    for ship_size in ship_sizes:
        placed = False
        while not placed:
            orientation = random.choice(['horizontal', 'vertical'])
            if orientation == 'horizontal':
                x = random.randint(0, board_size - 1)
                y = random.randint(0, board_size - ship_size)
            else:
                x = random.randint(0, board_size - ship_size)
                y = random.randint(0, board_size - 1)

            if is_valid_placement(x, y, ship_size, orientation):
                for i in range(ship_size):
                    if orientation == 'horizontal':
                        board[x][y + i] = 'S'
                        mark_empty_cells(x, y + i)
                    else:
                        board[x + i][y] = 'S'
                        mark_empty_cells(x + i, y)
                placed = True

    return board


# Пример использования:
board_size = 10
ship_sizes = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
game_board = place_ships(board_size, ship_sizes)

# Выводим доску с кораблями
for row in game_board:
    print(' '.join(row))