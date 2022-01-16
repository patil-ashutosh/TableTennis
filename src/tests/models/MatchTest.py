import unittest
from service.GameService import Game
from common import constants


class MatchTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()
    
    def test_number_of_sets_in_match(self):
        expected_sets_in_match = constants.DEFAULT_SETS_IN_MATCH
        self.assertEqual(self.game.match.num_of_sets_in_match, expected_sets_in_match)

    def test_score_to_win_set(self):
        expected_score_to_win_set = constants.DEFAULT_SCORE_TO_WIN_SET
        self.assertEqual(self.game.match.score_to_win_set, expected_score_to_win_set)

    def test_max_score_in_set(self):
        expected_max_score_in_test = constants.DEFAULT_MAX_SCORE_IN_SET
        self.assertEqual(self.game.match.max_score, expected_max_score_in_test)

    def test_get_match_scorecard(self):
        self.assertEqual(self.game.match.get_match_scorecard, [])

    