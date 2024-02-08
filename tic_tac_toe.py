
import sys  # Импорт модуля sys для работы с системными параметрами и стандартными потоками ввода
# Без этого модуля некорректно выводит (нашел решение с помощью StackOverflow)

# Настройка стандартного вывода для использования кодировки UTF-8 без автоматического закрытия файла
sys.stdout = open(1, 'w', encoding="utf-8", closefd=False)
# Настройка стандартного ввода для использования кодировки UTF-8 без автоматического закрытия файла
sys.stdin = open(0, 'r', encoding="utf-8", closefd=False)

# Создание пустого поля для игры в крестики-нолики
board = list(range(1, 10))

# Печать игрового поля
def print_field():
    print("-" * 13)
    for i in range(3):
        print(f"| {board[i * 3]} | {board[1 + i * 3]} | {board[2 + i * 3]} |")
        print("-" * 13)

# Ввод от игрока для установки символов X или O на поле
def take_input(player):
    while True:
        player_input = input(f"Игрок {player}, введите номер клетки: ")
        
        # Проверка является ли то, что ввел пользователем, если да, то отрабатывает if, иначе else
        if player_input.isdigit():
            player_input = int(player_input)
            if 1 <= player_input <= 9 and str(board[player_input - 1]) not in "XO":
                board[player_input - 1] = player
                break
            else:
                print("Ошибка: клетка занята или введено некорректное число. Попробуйте снова.")
        else:
            print("Ошибка: Введите число от 1 до 9.")

# Проверка на выигрыш
def check_win(player):
    # Комбинации для победы
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    # Проходим по всем возможным комбинациям для победы
    for combo in win_combinations:
        # Проверяем, совпадают ли значения на клетках для данной комбинации и символ игрока
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            # Если условие выполнено, возвращаем True (есть победа)
            return True
        # Если ни одна из комбинаций не соответствует, возвращаем False (победы нет)
    return False

# Основная функция игры
def play_game():
    players = ['X', 'O']
    for turn in range(10):  # в игре максимум 9 ходов
        current_player = players[turn % 2]
        print_field()
        take_input(current_player)
        if check_win(current_player):
            print_field()
            print(f"Игрок {current_player} победил!")
            return 
    print_field()
    print("Ничья!")

# Запуск игры
play_game()

            
            
            
            
            