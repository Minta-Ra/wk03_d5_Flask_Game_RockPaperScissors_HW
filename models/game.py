from models.player import Player

class Game():

    # Method to play game, passing both players
    def play_game(player_1, player_2):

        # Define variables
        roc = "rock"
        pap = "paper"
        sci = "scissors"

        # Rock, Paper, Scissors all options
        if player_1.choice == roc and player_2.choice == roc:
            return (f"It is a draw! Both players chose to play {player_1.choice}")
        elif player_1.choice == pap and player_2.choice == pap:
            return (f"It is a draw! Both players chose to play {player_1.choice}")
        elif player_1.choice == sci and player_2.choice == sci:
            return (f"It is a draw! Both players chose to play {player_1.choice}")

        elif player_1.choice == roc and player_2.choice == pap:
            return (f"{player_2.name} wins the game by playing {player_2.choice}")
        elif player_1.choice == pap and player_2.choice == roc:
            return (f"{player_1.name} wins the game by playing {player_1.choice}")

        elif player_1.choice == pap and player_2.choice == sci:
            return (f"{player_2.name} wins the game by playing {player_2.choice}")
        elif player_1.choice == sci and player_2.choice == pap:
            return (f"{player_1.name} wins the game by playing {player_1.choice}")

        elif player_1.choice == sci and player_2.choice == roc:
            return (f"{player_2.name} wins the game by playing {player_2.choice}")
        elif player_1.choice == roc and player_2.choice == sci:
            return (f"{player_1.name} wins the game by playing {player_1.choice}")