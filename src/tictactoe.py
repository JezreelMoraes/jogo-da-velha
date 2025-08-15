import sys

from PyQt5.QtWidgets import QApplication

from resources.core.tictactoe_core import TicTacToeCore
from resources.presentation.tictactoe_cli import TicTacToeCli
from resources.presentation.tictactoe_desktop import TicTacToeDesktop


class TicTacToe:

    @staticmethod
    def startCli():
        core = TicTacToeCore()
        cli = TicTacToeCli(core)
        cli.run()

    @staticmethod
    def startDesktop():
        app = QApplication(sys.argv)
        core = TicTacToeCore()
        desktop = TicTacToeDesktop(app, core)
        desktop.run()

    @staticmethod
    def startWeb():
        raise NotImplementedError("WEB mode is not implemented yet.")


if __name__ == '__main__':
    pass
