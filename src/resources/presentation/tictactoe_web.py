from flask import Flask, render_template_string, request, session

from resources.core.tictactoe_core import TicTacToeCore

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Jogo da Velha Web</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .grid { display: grid; grid-template-columns: repeat(3, 80px); grid-gap: 5px; margin: 20px auto; width: max-content; }
        .cell { width: 80px; height: 80px; font-size: 2em; text-align: center; }
        .info { margin: 10px auto; text-align: center; }
        .restart { margin: 10px auto; display: block; }
    </style>
</head>
<body>
    <div class="info">{{ info }}</div>
    <form method="post">
        <div class="grid">
            {% for i in range(9) %}
                <button class="cell" name="move" value="{{ i }}" {% if winner or board[i] != 0 %}disabled{% endif %}>{{ symbols[board[i]] }}</button>
            {% endfor %}
        </div>
        <button class="restart" name="restart" value="1">Reiniciar</button>
    </form>
    {% if message %}
        <div class="info" style="color: red;">{{ message }}</div>
    {% endif %}
</body>
</html>
"""


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
            idx = int(request.form['move'])
            row, col = divmod(idx, 3)

            if not core.play_move(row, col):
                message = "Movimento inválido!"

        save_core(core)

    info = f"Vez do jogador: {'X' if core.current_player == 1 else 'O'}"

    if core.winner:
        info = f"Jogador {'X' if core.winner == 1 else 'O'} venceu!"

    symbols = {0: ' ', 1: 'X', -1: 'O'}

    return render_template_string(
        HTML_TEMPLATE,
        board=core.board,
        symbols=symbols,
        info=info,
        winner=core.winner,
        message=message
    )
