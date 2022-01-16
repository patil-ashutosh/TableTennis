import unittest
from models.Player import SinglesPlayer, DoublesPlayer


class PlayerTest(unittest.TestCase):

    def test_set_singles_match_players_name(self):
        player_name = "Ashutosh"
        singles_match_players = SinglesPlayer(player_name)
        self.assertEqual(singles_match_players.players_names, [player_name])

    def test_set_doubles_match_players_name(self):
        player_one, player_two = "Ashutosh", "Prashant"
        doubles_match_players = DoublesPlayer(player_one, player_two)
        self.assertEqual(doubles_match_players.players_names, [player_one, player_two])
