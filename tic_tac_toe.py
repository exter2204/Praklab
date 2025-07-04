def print_board(board):
    print("  1 2 3")
    for i, row in enumerate(board):
        print(f"{i + 1} {' '.join(row)}")


def check_winner(board):
    # Проверка строк и столбцов
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # Ничья
    if all(cell != " " for row in board for cell in row):
        return "Draw"

    return None


def is_valid_move(board, x, y):
    return 0 <= x < 3 and 0 <= y < 3 and board[x][y] == " "


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Добро пожаловать в игру 'Крестики-нолики'!")
    print_board(board)

    while True:
        try:
            move = input(f"Игрок {current_player}, введите координаты (строка и столбец от 1 до 3, через пробел): ")
            row_str, col_str = move.strip().split()
            row, col = int(row_str) - 1, int(col_str) - 1

            if not is_valid_move(board, row, col):
                print("Некорректный ход. Попробуйте снова.")
                continue

            board[row][col] = current_player
            print_board(board)

            result = check_winner(board)
            if result == "X" or result == "O":
                print(f"Победил игрок {result}!")
                break
            elif result == "Draw":
                print("Ничья!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Ошибка ввода. Введите два числа через пробел.")


if __name__ == "__main__":
    main()
