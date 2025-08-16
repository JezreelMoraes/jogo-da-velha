from resources.core.constants import BOARD_SIZE


class BoardPosition:

    _INDEX_BOUND = BOARD_SIZE ** 2
    _BOARD_BOUND = BOARD_SIZE

    @property
    def index(self):
        return self._index

    @property
    def row(self):
        return self._row

    @property
    def column(self):
        return self._column

    def __init__(self, *, index: int = None, row: int = None, column: int = None):
        if index is not None:
            self._build_from_index(index)
        else:
            self._build_from_row_column(row, column)

    def _build_from_index(self, index: int):
        self._validate_index(index)

        self._index = index
        self._row, self._column = divmod(index, self._BOARD_BOUND)

    def _build_from_row_column(self, row: int, column: int):
        self._validate_board_size(row)
        self._validate_board_size(column)

        self._row = row
        self._column = column
        self._index = row * self._BOARD_BOUND + column

    def _validate_index(self, index: int):
        if index < 0:
            self._raise_out_of_bounds()

        if index >= self._INDEX_BOUND:
            self._raise_out_of_bounds()

    def _validate_board_size(self, board_size: int):
        if board_size < 0:
            self._raise_out_of_bounds()

        if board_size >= self._BOARD_BOUND:
            self._raise_out_of_bounds()

    def _raise_out_of_bounds(self):
        raise ValueError("Position is out of bounds.")

    def __str__(self):
        return f"BoardPosition(row={self._row}, column={self._column}, index={self._index})#{id(self)}"
