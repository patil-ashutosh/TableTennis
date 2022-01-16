import unittest


from exceptions import exceptions
from service.GameService import Game
from models.Match import MatchType, Match
from common import constants



class NegativeTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
    
    def test_create_team_with_invalid_match_type(self):
        self.assertRaises(exceptions.InvalidMatchTypeException, self.game.create_team, "TeamA", ("Ashutosh"), match_type= "triple")

    def test_create_doubles_team_with_invalid_names(self):
        self.assertRaises(exceptions.InvalidPlayersNameException, self.game.create_team, "TeamA", ("Ashutosh",), match_type=MatchType.doubles.name)

    def test_create_singles_team_with_invalid_names(self):
        self.assertRaises(exceptions.InvalidPlayersNameException, self.game.create_team, "TeamA", "")
    
    def test_play_match_when_match_is_already_over(self):
        self.game.create_team("Team-A", "Ashutosh")
        self.game.create_team("Team-B", "Sujit")
        self.game.play_match()
        self.assertRaises(exceptions.MatchIsAlreadyOverException, self.game.play_match)

    def test_match_with_even_num_of_sets(self):
        self.assertRaises(exceptions.MatchSetsEvenException, Match, match_type=constants.DEFAULT_MATCH_TYPE, num_of_sets=2, score_to_win=11, max_score=21)
    
    def test_match_with_invalid_score_to_win(self):
        self.assertRaises(exceptions.NumberNegativeException, Match, match_type=constants.DEFAULT_MATCH_TYPE, num_of_sets=1, score_to_win=0, max_score=21)

