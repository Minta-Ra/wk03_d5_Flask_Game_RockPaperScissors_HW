import unittest
from models.player import Player
from models.game import Game


class GameTest(unittest.TestCase):
    def setUp(self):
        # Player objects
        self.player_1 = Player("Marry", "paper")
        self.player_2 = Player("Harry", "rock")
        # players = [player_1, player_2]


    def test_game_logic(self):
        expected = Game.play_game(self.player_1, self.player_2)
        actual = "Marry wins the game by choosing playing paper"
        self.assertEqual(expected, actual)