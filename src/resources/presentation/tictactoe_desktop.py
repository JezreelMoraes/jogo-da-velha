import sys

from PyQt5.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                             QMainWindow, QMessageBox, QPushButton,
                             QVBoxLayout, QWidget)

from resources.core.board_position import BoardPosition
from resources.core.constants import BOARD_SIZE
from resources.core.tictactoe_core import TicTacToeCore


class TicTacToeDesktop(QMainWindow):

    _SYMBOLS = {
        TicTacToeCore.EMPTY: ' ',
        TicTacToeCore.PLAYER_X: 'X',
        TicTacToeCore.PLAYER_O: 'O'
    }

    def __init__(self, app: QApplication, core: TicTacToeCore):
        super().__init__()
        self._core = core
        self._app = app

        self.setWindowTitle("Jogo da Velha")

        self._central_widget = QWidget()
        self.setCentralWidget(self._central_widget)
        self.layout = QVBoxLayout()
        self._central_widget.setLayout(self.layout)

        self._info_label = QLabel()
        self.layout.addWidget(self._info_label)

        self._grid_layout = QGridLayout()
        self.layout.addLayout(self._grid_layout)

        self._buttons = []
        for row in range(BOARD_SIZE):
            for column in range(BOARD_SIZE):

                button = QPushButton("")
                button.setMinimumSize(80, 80)

                button.setSizePolicy(
                    button.sizePolicy().Expanding,
                    button.sizePolicy().Expanding
                )

                position = BoardPosition(row=row, column=column)
                button.clicked.connect(
                    lambda _, button=button, position=position: self._handle_move(button, position)
                )

                self._grid_layout.addWidget(button, row, column)
                self._buttons.append(button)

        self._restart_btn = QPushButton("Reiniciar")
        self._restart_btn.clicked.connect(self._start)

        footer = QHBoxLayout()
        footer.addStretch()
        footer.addWidget(self._restart_btn)

        self.layout.addLayout(footer)

    def run(self):
        self._start()
        self.show()
        sys.exit(self._app.exec_())

    def _handle_move(self, button: QPushButton, position: BoardPosition):
        if self._core.winner:
            return

        if not self._core.play_move(position):
            QMessageBox.warning(
                self,
                "Movimento inválido",
                "Essa posição já está ocupada ou o movimento é inválido."
            )

            return

        self._update_button_label(button, position)

        if self._core.winner:
            self._info_label.setText(
                f"Jogador { self._get_player_symbol(self._core.winner) } venceu!"
            )

            QMessageBox.information(
                self,
                "Fim de jogo",
                f"Jogador { self._get_player_symbol(self._core.winner) } venceu!"
            )
        else:
            current_player = self._SYMBOLS[self._core.current_player]
            self._info_label.setText(f"Vez do jogador: {current_player}")

    def _update_button_label(self, button: QPushButton, position: BoardPosition):
        player = self._core.get_position_value(position)
        player_symbol = self._get_player_symbol(player)
        button.setText(player_symbol)

    def _get_player_symbol(self, player) -> str:
        return self._SYMBOLS[player]

    def _update_current_player_label(self):
        player_symbol = self._get_player_symbol(self._core.current_player)
        self._info_label.setText(f"Vez do jogador: { player_symbol }")

    def _start(self):
        self._core.start()
        self._update_current_player_label()

        for button in self._buttons:
            button.setText("")
