import os

from resources.core.tictactoe_core import TicTacToeCore


class TicTacToeCli:

    CLEAR_COMMAND = 'cls' if os.name == 'nt' else 'clear'

    BOARD_COLUMN_DIVISOR = ' | '
    BOARD_ROW_DIVISOR = '-' * 9 + '\n'

    SYMBOLS = {
        TicTacToeCore.EMPTY: ' ',
        TicTacToeCore.PLAYER_X: 'X',
        TicTacToeCore.PLAYER_O: 'O'
    }

    def __init__(self, core: TicTacToeCore):
        self.core = core

    def _clean_console(self) -> None:
        os.system(self.CLEAR_COMMAND)

    def _get_player_symbol(self, player) -> str:
        return self.SYMBOLS[player]

    def _print_board(self) -> None:
        self._clean_console()

        board_rows_list = []
        for row in range(3):
            board_columns_list = []

            for column in range(3):
                player = self.core.get_position_value(row, column)
                player_symbol = self._get_player_symbol(player)
                board_columns_list.append(player_symbol)

            board_rows_list.append(
                self.BOARD_COLUMN_DIVISOR.join(board_columns_list) + '\n'
            )

        print(self.BOARD_ROW_DIVISOR.join(board_rows_list))

    def run(self) -> None:
        self.core.start()

        while not self.core.winner:
            self._print_board()

            row = int(input("Enter row (0-2): "))
            column = int(input("Enter column (0-2): "))

            if not self.core.play_move(row, column):
                input("\nInvalid move. Try again.")
                continue

        self._print_board()
        print(f"Player { self._get_player_symbol(self.core.winner) } wins!")
