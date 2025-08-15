class TicTacToeCore:

    EMPTY = 0
    PLAYER_X = 1
    PLAYER_O = -1

    _BOARD_POSITION_BOUND = 9
    _WIN_CONDITION = 3

    def __init__(self):
        self.start()

    def start(self) -> None:
        self.board = [self.EMPTY for _ in range(self._BOARD_POSITION_BOUND)]
        self.current_player = self.PLAYER_X
        self.winner = None

    def can_play_move(self, row: int, column: int) -> bool:
        board_position = row * 3 + column
        if (board_position >= self._BOARD_POSITION_BOUND):
            return False

        return self.board[board_position] == self.EMPTY

    def play_move(self, row: int, column: int) -> bool:
        if not self.can_play_move(row, column):
            return False

        board_position = row * 3 + column
        self.board[board_position] = self.current_player

        if self._check_winner():
            self.winner = self.current_player
            return True

        self._switch_player()

        return True

    def get_position_value(self, row: int, column: int) -> int:
        board_position = row * 3 + column
        if (board_position >= self._BOARD_POSITION_BOUND):
            raise IndexError("Invalid board position")

        return self.board[board_position]

    def _check_winner(self) -> bool:
        diagonal_sum = self.board[0] + self.board[4] + self.board[8]
        if abs(diagonal_sum) == self._WIN_CONDITION:
            return True

        diagonal_sum = self.board[2] + self.board[4] + self.board[6]
        if abs(diagonal_sum) == self._WIN_CONDITION:
            return True

        for index in range(3):
            horizontal_sum = sum(self.board[index*3:index*3+3])
            if abs(horizontal_sum) == self._WIN_CONDITION:
                return True

            vertical_sum = sum(self.board[index::3])
            if abs(vertical_sum) == self._WIN_CONDITION:
                return True

    def _switch_player(self):
        self.current_player *= -1


if __name__ == '__main__':
    pass
