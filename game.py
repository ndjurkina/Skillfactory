def print_field(field):
    """
    Печатает игровое поле в консоль
    """
    print('    0   1   2')
    print('----------------')
    for i, row in enumerate(field):
        print(f'{i} |', end="")
        for cell in row:
            print(f' {cell} |', end="")
        print('\n----------------')


def check_win(field):
    # проверка строк
    for row in field:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
        # столбцы
    for col in range(3):
        if field[0][col] == field[1][col] == field[2][col] != ' ':
            return field[0][col]
            # диагонали
    if field[0][0] == field[1][1] == field[2][2] != ' ':
        return field[0][0]
    if field[2][0] == field[1][1] == field[0][2] != ' ':
        return field[2][0]
        # ничья
    for row in field:
        for cell in row:
            if cell == ' ':
                return None  # игра продолжается
    return 'ничья'


def get_player_move(field):
    """Получает ход игрока от пользователя."""
    while True:
        move_input = input("Введите координаты хода (строка, столбец): ")
        parts = move_input.split()
        if len(parts) != 2:
            print("Некорректный ввод. Введите два числа, разделенные пробелом.")
            continue
        if not parts[0].isdigit() or not parts[1].isdigit():
            print('Некорректный ввод. Введите число.')
            continue
        row = int(parts[0])
        col = int(parts[1])
        if 0 <= row < 3 and 0 <= col < 3 and field[row][col] == ' ':
            return row, col
        else:
            print("Неверные координаты. Координаты за пределами доски или клетка занята.")

def play_game():
    field = [[' ']*3 for i in range(3)]
    player = 'X'
    while True:
        print_field(field)
        print(f' ходит {player}')
        row, col = get_player_move(field)
        field[row][col] = player
        res = check_win(field)
        if res:
            if res == 'ничья':
                print('Ничья')
            else:
                print(f' победил {player}')
            print_field(field)
            return
        player = 'X' if player == '0' else '0'

play_game()
