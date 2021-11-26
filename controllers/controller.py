from flask import render_template, request, redirect
from app import app
from models.player import Player
from models.all_players import players
from models.game import players, play_game


@app.route("/")
def index():
    return render_template("index.html", title="Home", players=players)


@app.route("/<choice_1>/<choice_2>")
def game(choice_1, choice_2):
    player_1 = Player("John", choice_1)
    player_2 = Player("Rachel", choice_2)

    winner = play_game(player_1, player_2)

    return render_template("index.html", title="Home", winner=winner)
