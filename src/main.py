import os

BOARD_POSITION_BOUND = 9

EMPTY = 0
PLAYER_X = 1
PLAYER_O = -1

SYMBOLS = {EMPTY: ' ', PLAYER_X: 'X', PLAYER_O: 'O'}

WIN_CONDITION = 3

def can_play_move(board: list[int], row: int, column: int) -> bool:
    board_position = row * 3 + column
    if (board_position >= BOARD_POSITION_BOUND): 
        return False
    
    return board[board_position] == EMPTY

def play_move(board: list[int], row: int, column: int, player: int) -> bool:
    if not can_play_move(board, row, column):
        return False
    
    board_position = row * 3 + column
    board[board_position] = player

    return True

def has_winner(board) -> bool:
    diagonal_sum = board[0] + board[4] + board[8]
    if abs(diagonal_sum) == WIN_CONDITION:
        return True
    
    diagonal_sum = board[2] + board[4] + board[6]
    if abs(diagonal_sum) == WIN_CONDITION:
        return True

    for index in range(3):
        horizontal_sum = sum(board[index*3:index*3+3])
        if abs(horizontal_sum) == WIN_CONDITION:
            return True
        
        vertical_sum = sum(board[index::3])
        if abs(vertical_sum) == WIN_CONDITION:
            return True


def clean_console() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board(board: list[int]) -> None:
    clean_console()
    
    board_rows_list = []

    for row in range(3):
        board_columns_list = []

        for column in range(3):
            board_position = row * 3 + column

            player_symbol = SYMBOLS[board[board_position]]
            board_columns_list.append(player_symbol)

        board_rows_list.append(' | '.join(board_columns_list) + '\n')

    divisor = '-' * 9 + '\n'
    print(divisor.join(board_rows_list))


if __name__ == '__main__':
    board = [EMPTY for _ in range(BOARD_POSITION_BOUND)]
    current_player = PLAYER_X

    while not has_winner(board):
        print_board(board)

        player_symbol = SYMBOLS[current_player]
        row = int(input(f'Jogador {player_symbol}, escolha a linha (0, 1, 2): '))
        column = int(input(f'Jogador {player_symbol}, escolha a coluna (0, 1, 2): '))

        if not play_move(board, row, column, current_player):
            print('\nMovimento inválido! Tente novamente.')
            input('Pressione Enter para continuar...')
            continue

        current_player *= -1

    print_board(board)
    print(f'Jogador {SYMBOLS[current_player * -1]} venceu!')