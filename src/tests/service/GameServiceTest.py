import unittest
from itertools import cycle

from service.GameService import Game
from models.Match import MatchType
from models import Serve


from common import constants


class GameServiceTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_play_match(self):
        self.game.create_team("Team-A", "Ashutosh")
        self.game.create_team("Team-B", "Sujit")
        self.game.play_match()
        self.assertTrue(self.game.game_completed)
        self.assertTrue(self.game.match.is_match_over)
        self.assertIsNotNone(self.game.match.winner_team_name)

    def test_play_doubles_match(self):
        self.game.create_team("Team-A", ("Ashutosh","Sujit"), match_type=MatchType.doubles.name)
        self.game.create_team("Team-B", ("Prashant", "Suraj"), match_type=MatchType.doubles.name)
        self.game.play_match()
        self.assertTrue(self.game.game_completed)
        self.assertTrue(self.game.match.is_match_over)
        self.assertIsNotNone(self.game.match.winner_team_name)

    def test_play_match_with_even_serve(self):
        serve = Serve.EvenServe()
        self.game.set_serve(serve)
        self.game.create_team("Team-A", "Ashutosh")
        self.game.create_team("Team-B", "Sujit")
        self.game.play_match()
        winner_team = self.game.match.winner_team_name
        teams = self.game.get_teams
        score = teams[winner_team].score
        self.assertEqual(score, ['11-0'])

    def test_play_match_with_odd_serve(self):
        serve = Serve.OddServe()
        self.game.set_serve(serve)
        self.game.create_team("Team-A", "Ashutosh")
        self.game.create_team("Team-B", "Sujit")
        self.game.play_match()
        winner_team = self.game.match.winner_team_name
        teams = self.game.get_teams
        score = teams[winner_team].score
        self.assertEqual(score, ['11-0'])

    def test_play_match_when_points_tied_at_duece_score(self):
        self.game.create_team("Team-A", "Ashutosh")
        self.game.create_team("Team-B", "Sujit")
        team_one, team_two = self.game.team_names
        self.game.match.curr_score_of_set[team_one] = self.game.match.deuce_score
        self.game.match.curr_score_of_set[team_two] = self.game.match.deuce_score
        self.game.service_flag = 1
        self.game.pool = cycle([team_one, team_two])
        self.game.handle_deuce_score_condition(team_one, team_two)
        self.game.match.update_match_scorecard(( self.game.match.curr_score_of_set[team_one], self.game.match.curr_score_of_set[team_two]))
        sets_won = {team_one:0, team_two:0}
        if self.game.check_winner_of_sets( self.game.match.curr_score_of_set[team_one], self.game.match.curr_score_of_set[team_two]) == 0:
            sets_won[team_one]+=1
        else:
            sets_won[team_two]+=1
        self.game.update_teams_sets_win_details(sets_won)
        self.game.update_match_winner_details()
        self.game.update_teams_scores_details()
        winner_team = self.game.match.winner_team_name
        print(self.game.match.curr_score_of_set)
        diff_of_points = abs(self.game.match.curr_score_of_set[team_one] - self.game.match.curr_score_of_set[team_two])
        self.assertEqual(diff_of_points, 2)

    def test_play_match_when_points_tied_below_max_score(self):
        self.game.create_team("Team-A", "Ashutosh")
        self.game.create_team("Team-B", "Sujit")
        team_one, team_two = self.game.team_names
        self.game.match.curr_score_of_set[team_one] = constants.DEFAULT_MAX_SCORE_IN_SET-1
        self.game.match.curr_score_of_set[team_two] = constants.DEFAULT_MAX_SCORE_IN_SET-1
        self.game.service_flag = 1
        self.game.pool = cycle([team_one, team_two])

        self.game.handle_deuce_score_condition(team_one, team_two)
        self.game.match.update_match_scorecard(( self.game.match.curr_score_of_set[team_one], self.game.match.curr_score_of_set[team_two]))
        sets_won = {team_one:0, team_two:0}
        if self.game.check_winner_of_sets( self.game.match.curr_score_of_set[team_one], self.game.match.curr_score_of_set[team_two]) == 0:
            sets_won[team_one]+=1
        else:
            sets_won[team_two]+=1
        self.game.update_teams_sets_win_details(sets_won)
        self.game.update_match_winner_details()
        self.game.update_teams_scores_details()
        winner_team = self.game.match.winner_team_name
        print(self.game.match.curr_score_of_set)
        diff_of_points = abs(self.game.match.curr_score_of_set[team_one] - self.game.match.curr_score_of_set[team_two])
        self.assertEqual(diff_of_points, 1)

