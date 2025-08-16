from flask import Flask, render_template, request, session

from resources.core.board_position import BoardPosition
from resources.core.constants import BOARD_SIZE
from resources.core.tictactoe_core import TicTacToeCore

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

_SYMBOLS = {
    TicTacToeCore.EMPTY: ' ',
    TicTacToeCore.PLAYER_X: 'X',
    TicTacToeCore.PLAYER_O: 'O'
}


def get_core():
    core = TicTacToeCore()

    if 'board' not in session:
        core.start()
        session['board'] = core.board
        session['current_player'] = core.current_player
        session['winner'] = core.winner
    else:
        core.board = session['board']
        core.current_player = session['current_player']
        core.winner = session['winner']

    return core


def save_core(core):
    session['board'] = core.board
    session['current_player'] = core.current_player
    session['winner'] = core.winner


@app.route("/", methods=["GET", "POST"])
def index():
    core = get_core()
    message = ""

    if request.method == "POST":
        if 'restart' in request.form:
            core.start()
            message = ""

        elif 'move' in request.form and not core.winner:
            index = int(request.form['move'])

            position = BoardPosition(index=index)
            if not core.play_move(position):
                message = "Movimento inválido!"

        save_core(core)

    info = f"Vez do jogador: {_SYMBOLS[core.current_player]}"

    if core.winner:
        info = f"Jogador {_SYMBOLS[core.winner]} venceu!"

    return render_template(
        "index.jinja2",
        board=core.board,
        board_size=BOARD_SIZE,
        symbols=_SYMBOLS,
        info=info,
        winner=core.winner,
        message=message
    )
