import sys

from PyQt5.QtWidgets import QApplication

from resources.core.tictactoe_core import TicTacToeCore
from resources.presentation.tictactoe_cli import TicTacToeCli
from resources.presentation.tictactoe_desktop import TicTacToeDesktop
from resources.presentation.tictactoe_web import app


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
        app.run(debug=True)
