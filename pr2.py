def print_board(board):
    
    Args:
        board (list): Список из 9 элементов, представляющих состояние поля.
    """
    print("\nТекущее состояние поля:\n")
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")
    print()

def check_game_over(board):
    
    Args:
        board (list): Список из 9 элементов, представляющих состояние поля.
    
    Returns:
        str/None: Возвращает 'X' или 'O' если есть победитель, 
                 'draw' если ничья, None если игра продолжается.
    """
    # Выигрышные комбинации
    win_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтальные
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикальные
        [0, 4, 8], [2, 4, 6]               # Диагональные
    ]
    
    for line in win_lines:
        if board[line[0]] == board[line[1]] == board[line[2]] != " ":
            return board[line[0]]  # Возвращаем победителя
    
    if " " not in board:
        return "draw"  # Ничья
    
    return None  # Игра продолжается


def get_valid_move(board, current_player):
    
    Args:
        board (list): Текущее состояние игрового поля.
        current_player (str): Текущий игрок ('X' или 'O').
    
    Returns:
        int: Индекс выбранной клетки (0-8).
    """
    while True:
        try:
            move = input(f"Игрок {current_player}, введите номер клетки (1-9): ")
            
            # Проверка на пустой ввод
            if not move:
                print("Ошибка: Введите число от 1 до 9!")
                continue
                
            move = int(move) - 1  # Преобразуем в индекс (0-8)
            
            # Проверка диапазона
            if move < 0 or move > 8:
                print("Ошибка: Число должно быть от 1 до 9!")
                continue
                
            # Проверка доступности клетки
            if board[move] != " ":
                print("Ошибка: Эта клетка уже занята!")
                continue
                
            return move
            
        except ValueError:
            print("Ошибка: Пожалуйста, введите число от 1 до 9!")


def switch_player(current_player):
    """Меняет текущего игрока.
    
    Args:
        current_player (str): Текущий игрок ('X' или 'O').
    
    Returns:
        str: Следующий игрок.
    """
    return "O" if current_player == "X" else "X"


def show_help():
    print("\nПравила игры:")
    print("1. Игроки по очереди ставят X или O в свободные клетки поля.")
    print("2. Первый, выстроивший 3 своих фигуры в ряд (по горизонтали,")
    print("   вертикали или диагонали) - выигрывает.")
    print("3. Если все клетки заполнены, но нет победителя - ничья.")
    print("\nНумерация клеток:")
    print_board([str(i+1) for i in range(9)])
    print()


def play_game():
    """Основная функция игры."""
    board = [" "] * 9  # Пустое поле 3x3
    current_player = "X"
    game_result = None
    
    print("\nДобро пожаловать в игру 'Крестики-нолики'!")
    show_help()
    
    while not game_result:
        print_board(board)
        move = get_valid_move(board, current_player)
        board[move] = current_player
        
        game_result = check_game_over(board)
        
        if game_result:
            print_board(board)
            if game_result == "draw":
                print("Игра окончена! Ничья!")
            else:
                print(f"Поздравляем! Игрок {game_result} победил!")
        else:
            current_player = switch_player(current_player)


def main():
    """Точка входа в программу."""
    while True:
        play_game()
        
        # Запрос на повторную игру
        while True:
            choice = input("\nХотите сыграть ещё раз? (да/нет): ").lower()
            if choice in ("да", "д", "yes", "y"):
                print("\nНачинаем новую игру!")
                break
            elif choice in ("нет", "н", "no", "n"):
                print("\nСпасибо за игру! До свидания!")
                return
            else:
                print("Пожалуйста, введите 'да' или 'нет'.")


if __name__ == "__main__":
    main()
