from flask import render_template, request, redirect
from app import app
from models.player import Player
from models.game import Game
import random


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


#################################################


# Play page
@app.route("/play")
def play():
    return render_template("play.html")


# Play against computer
@app.route("/playgame", methods=["POST"])
def play_game():
    # Player Human
    player_1_name = request.form.get("name")
    player_1_choice = request.form.get("choice")
    player_1 = Player(player_1_name, player_1_choice)

    # Player Computer
    list = ["rock", "paper", "scissors"]
    random_choice = random.choice(list)
    player_2 = Player("Computer", random_choice)
    players = [player_1, player_2]

    winner_hc = Game.play_game(player_1, player_2)
    
    return render_template("winner.html", title="Winner", winner=winner_hc, players=players)