from models.player import Player
from models.all_players import players

# class Game():

# Method to play game, passing both players
def play_game(player_1, player_2):

    print("   ")
    print("   ")
    print(player_1.choice)
    print(player_2.choice)
    print("   ")
    print("   ")

    roc = "rock"
    pap = "paper"
    sci = "scissors"


    if player_1.choice == roc and player_2.choice == roc:
        print(f"It is a draw! Both players chose to play {player_1.choice}")
    elif player_1.choice == pap and player_2.choice == pap:
        print(f"It is a draw! Both players chose to play {player_1.choice}")
    elif player_1.choice == sci and player_2.choice == sci:
        print(f"It is a draw! Both players chose to play {player_1.choice}")

    elif player_1.choice == roc and player_2.choice == pap:
        print(f"{player_2.name} wins the game by choosing playing {player_2.choice}")
    elif player_1.choice == pap and player_2.choice == roc:
        print(f"{player_1.name} wins the game by choosing playing {player_1.choice}")

    elif player_1.choice == pap and player_2.choice == sci:
        print(f"{player_2.name} wins the game by choosing playing {player_2.choice}")
    elif player_1.choice == sci and player_2.choice == pap:
        print(f"{player_1.name} wins the game by choosing playing {player_1.choice}")

    elif player_1.choice == sci and player_2.choice == roc:
        print(f"{player_2.name} wins the game by choosing playing {player_2.choice}")
    elif player_1.choice == roc and player_2.choice == sci:
        print(f"{player_1.name} wins the game by choosing playing {player_1.choice}")