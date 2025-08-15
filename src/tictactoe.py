from resources.core.tictactoe_core import TicTacToeCore
from resources.presentation.tictactoe_cli import TicTacToeCli


class TicTacToe:

    @staticmethod
    def startCli():
        core = TicTacToeCore()
        cli = TicTacToeCli(core)
        cli.run()

    @staticmethod
    def startDesktop():
        raise NotImplementedError("Desktop mode is not implemented yet.")

    @staticmethod
    def startWeb():
        raise NotImplementedError("WEB mode is not implemented yet.")


if __name__ == '__main__':
    pass
