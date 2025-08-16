from resources.core.board_position import BoardPosition
from resources.core.constants import BOARD_SIZE


class TicTacToeCore:

    EMPTY = 0
    PLAYER_X = 1
    PLAYER_O = -1

    _WIN_CONDITION_SUM = BOARD_SIZE

    def __init__(self):
        self.start()

    def start(self) -> None:
        self.board = [self.EMPTY for _ in range(BOARD_SIZE ** 2)]
        self.current_player = self.PLAYER_X
        self.winner = None

    def can_play_move(self, position: BoardPosition) -> bool:
        return self.board[position.index] == self.EMPTY

    def play_move(self, position: BoardPosition) -> bool:
        if not self.can_play_move(position):
            return False

        self.board[position.index] = self.current_player

        if self._check_winner():
            self.winner = self.current_player
            return True

        self._switch_player()

        return True

    def get_position_value(self, position: BoardPosition) -> int:
        return self.board[position.index]

    def _check_winner(self) -> bool:
        diagonal_sum = sum(self.board[0::BOARD_SIZE + 1])
        if abs(diagonal_sum) == self._WIN_CONDITION_SUM:
            return True

        inverted_diagonal_sum = sum(self.board[BOARD_SIZE - 1::BOARD_SIZE - 1])
        if abs(inverted_diagonal_sum) == self._WIN_CONDITION_SUM:
            return True

        for index in range(BOARD_SIZE):
            horizontal_sum = sum(self.board[index * BOARD_SIZE:(index + 1) * BOARD_SIZE])
            if abs(horizontal_sum) == self._WIN_CONDITION_SUM:
                return True

            vertical_sum = sum(self.board[index::BOARD_SIZE])
            if abs(vertical_sum) == self._WIN_CONDITION_SUM:
                return True

    def _switch_player(self):
        self.current_player *= -1
