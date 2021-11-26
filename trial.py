
# Player objects
player_1 = "paper"
player_2 = "scissors"


# Method to play game, passing both players
def play_game(player_1, player_2):
    
    print("    ")
    print("    ")
    print(player_1)
    print("    ")
    print("    ")

    roc = "rock"
    pap = "paper"
    sci = "scissors"

    if player_1 == roc and player_2 == roc:
        print("It is a draw!")
    elif player_1 == pap and player_2 == pap:
        print("It is a draw!")
    elif player_1 == sci and player_2 == sci:
        print("It is a draw!")

    elif player_1 == roc and player_2 == pap:
        print(f"{player_2} wins the game")
    elif player_1 == pap and player_2 == roc:
        print(f"{player_1} wins the game")

    elif player_1 == pap and player_2 == sci:
        print(f"{player_2} wins the game")
    elif player_1 == sci and player_2 == pap:
        print(f"{player_1} wins the game")

    elif player_1 == sci and player_2 == roc:
        print(f"{player_2} wins the game")
    elif player_1 == roc and player_2 == sci:
        print(f"{player_1} wins the game")

play_game(player_1, player_2)