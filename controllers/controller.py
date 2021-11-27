from flask import render_template, request, redirect
from app import app
from models.player import Player
from models.game import Game


# Home page
@app.route("/")
def index():
    return render_template("index.html", title="Home")

# Winner page
@app.route("/<choice_1>/<choice_2>")
def game(choice_1, choice_2):
    player_1 = Player("Player 1", choice_1)
    player_2 = Player("Player 2", choice_2)
    players = [player_1, player_2]

    winner = Game.play_game(player_1, player_2)

    return render_template("winner.html", title="Winner", winner=winner, players=players)