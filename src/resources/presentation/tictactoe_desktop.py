import sys

from PyQt5.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                             QMainWindow, QMessageBox, QPushButton,
                             QVBoxLayout, QWidget)

from resources.core.tictactoe_core import TicTacToeCore


class TicTacToeDesktop(QMainWindow):

    SYMBOLS = {
        TicTacToeCore.EMPTY: ' ',
        TicTacToeCore.PLAYER_X: 'X',
        TicTacToeCore.PLAYER_O: 'O'
    }

    def __init__(self, app: QApplication, core: TicTacToeCore):
        super().__init__()
        self.core = core
        self.app = app

        self.setWindowTitle("Jogo da Velha")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.info_label = QLabel("Vez do jogador: X")
        self.layout.addWidget(self.info_label)

        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        self.buttons = []
        for row in range(3):
            for column in range(3):
                button = QPushButton("")
                button.setMinimumSize(80, 80)
                button.setSizePolicy(
                    button.sizePolicy().Expanding,
                    button.sizePolicy().Expanding
                )

                button.clicked.connect(
                    lambda _, index=row * 3 + column: self.handle_move(index)
                )

                self.grid_layout.addWidget(button, row, column)
                self.buttons.append(button)

        self.restart_btn = QPushButton("Reiniciar")
        self.restart_btn.clicked.connect(self.start)

        footer = QHBoxLayout()
        footer.addStretch()
        footer.addWidget(self.restart_btn)

        self.layout.addLayout(footer)
        self.update_board()

    def handle_move(self, index):
        row, col = divmod(index, 3)
        if self.core.winner:
            return

        if not self.core.play_move(row, col):
            QMessageBox.warning(
                self,
                "Movimento inválido",
                "Essa posição já está ocupada ou o movimento é inválido."
            )

            return

        self.update_board()
        if self.core.winner:
            self.info_label.setText(
                f"Jogador { self.SYMBOLS[self.core.winner] } venceu!"
            )

            QMessageBox.information(
                self,
                "Fim de jogo",
                f"Jogador { self.SYMBOLS[self.core.winner] } venceu!"
            )
        else:
            current = self.SYMBOLS[self.core.current_player]
            self.info_label.setText(f"Vez do jogador: {current}")

    def update_board(self):
        for idx, btn in enumerate(self.buttons):
            row, col = divmod(idx, 3)
            value = self.core.get_position_value(row, col)
            btn.setText(self.SYMBOLS[value])

    def start(self):
        self.core.start()
        self.info_label.setText("Vez do jogador: X")
        self.update_board()

    def run(self):
        self.start()
        self.show()
        sys.exit(self.app.exec_())
