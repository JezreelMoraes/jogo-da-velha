import os

from resources.core.board_position import BoardPosition
from resources.core.constants import BOARD_SIZE
from resources.core.tictactoe_core import TicTacToeCore


class TicTacToeCli:

    _CLEAR_COMMAND = 'cls' if os.name == 'nt' else 'clear'

    _BOARD_COLUMN_DIVISOR = ' | '

    _BOARD_ROW_DIVISOR = '-' * (
        len(_BOARD_COLUMN_DIVISOR) *
        (BOARD_SIZE - 1) +
        BOARD_SIZE
    ) + '\n'

    _SYMBOLS = {
        TicTacToeCore.EMPTY: ' ',
        TicTacToeCore.PLAYER_X: 'X',
        TicTacToeCore.PLAYER_O: 'O'
    }

    def __init__(self, core: TicTacToeCore):
        self._core = core

    def run(self) -> None:
        self._core.start()

        while not self._core.winner:
            self._print_board()

            try:
                row = int(input(
                    f'Player { self._current_player_symbol() }, enter row (0-{ BOARD_SIZE - 1 }): '
                ))

                column = int(input(
                    f'Player { self._current_player_symbol() }, enter column (0-{ BOARD_SIZE - 1 }): '
                ))

                position = BoardPosition(row=row, column=column)
                if self._core.play_move(position):
                    continue

            except ValueError:
                pass

            input("\nInvalid move. Try again.")

        self._print_board()
        print(f"Player { self._get_player_symbol(self._core.winner) } wins!")

    def _clean_console(self) -> None:
        os.system(self._CLEAR_COMMAND)

    def _get_player_symbol(self, player) -> str:
        return self._SYMBOLS[player]

    def _print_board(self) -> None:
        self._clean_console()

        board_rows_list = []
        for row in range(BOARD_SIZE):
            board_columns_list = []

            for column in range(BOARD_SIZE):
                position = BoardPosition(row=row, column=column)
                player = self._core.get_position_value(position)
                player_symbol = self._get_player_symbol(player)
                board_columns_list.append(player_symbol)

            board_rows_list.append(
                self._BOARD_COLUMN_DIVISOR.join(board_columns_list) + '\n'
            )

        print(self._BOARD_ROW_DIVISOR.join(board_rows_list))

    def _current_player_symbol(self) -> str:
        return self._get_player_symbol(self._core.current_player)
