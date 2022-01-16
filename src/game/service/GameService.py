#from models.Match import MatchType
from models.Match import Match
from models.Team import Team
from models.Player import DoublesPlayer
from models import Serve

from common import constants
from common import utils
from exceptions import exceptions
from itertools import cycle


class Game:
    def __init__(self, match_type=constants.DEFAULT_MATCH_TYPE, num_of_sets_in_match=constants.DEFAULT_SETS_IN_MATCH,
                 score_to_win=constants.DEFAULT_SCORE_TO_WIN_SET,
                 max_score=constants.DEFAULT_MAX_SCORE_IN_SET,
                 serve = Serve.RandomServe()):
        self._teams = {}
        self.match = Match(match_type=match_type, num_of_sets=num_of_sets_in_match, score_to_win=score_to_win, max_score=max_score)
        self.serve = serve
        self._game_completed= False

    @property
    def game_completed(self):
        return self._game_completed
    
    @game_completed.setter
    def game_completed(self, is_completed):
        self._game_completed = is_completed

    @property
    def team_names(self):
        return list(self._teams.keys())
    
    @property
    def get_teams(self):
        return self._teams

    def get_serve(self):
        return self.serve

    def set_serve(self, serve):
        self.serve = serve

    def create_team(self, team_name, players_name, match_type=constants.DEFAULT_MATCH_TYPE):
        team = Team(team_name)
        team.add_players_to_team(match_type, players_name)
        self.get_teams[team.name] = team

    def play_match(self):
        if self.match.is_match_over:
            raise exceptions.MatchIsAlreadyOverException()
        serve = self.serve
        teams = self.team_names
        team_one, team_two = teams[0], teams[1]
        num_of_sets = self.match.num_of_sets_in_match
        self.match.curr_score_of_set[team_one] = 0
        self.match.curr_score_of_set[team_two] = 0

        print(f"\nTeams playing match are: {team_one}, {team_two}")
        print(f"Number of sets in match: {num_of_sets}")
        print(f"Score required to win set: {self.match.score_to_win_set}")
        print("Match started ........\n")
    
        self.match.update_match_scorecard((team_one, team_two))
        sets_won_by_teams = self.play_all_sets_of_match(serve, team_one, team_two, num_of_sets)
        self.update_teams_sets_win_details(sets_won_by_teams)
        self.update_match_winner_details()
        self.update_teams_scores_details()
 

        self.display_match_winner()

    def play_all_sets_of_match(self, serve, team_one, team_two, num_of_sets):
        num_of_sets_to_win_match = self.match.num_of_sets_to_win_match
        sets_won = {team_one:0, team_two:0}
        for each_set in range(num_of_sets): 
            print(f"\n------- Playing Set {each_set+1} -------")
            self.play_each_sets(team_one, team_two)
            self.match.update_match_scorecard((self.match.curr_score_of_set[team_one], self.match.curr_score_of_set[team_two]))
            if self.check_winner_of_sets(self.match.curr_score_of_set[team_one], self.match.curr_score_of_set[team_two]) == 0:
                sets_won[team_one]+=1
            else:
                sets_won[team_two]+=1
            self.display_sets_winner(team_one, team_two)
            print(f"------- Set {each_set+1} Completed -------")
            if self.check_if_any_team_won_majority_of_sets(sets_won[team_one], sets_won[team_two], num_of_sets_to_win_match):
                break
            self.match.reset_curr_score_of_set()
        return sets_won

    def play_each_sets(self, team_one, team_two):
        score_to_win = self.match.score_to_win_set
        is_set_completed = False
        self.service_flag = 1
        self.pool = cycle([team_one, team_two])
        #is_have_service
        while is_set_completed is False:
            if self.check_if_deuce_exists(team_one, team_two):
                print("Duece Points, team with two-point lead to win the game")
                self.handle_deuce_score_condition(team_one, team_two)
                is_set_completed = True
            elif self.match.curr_score_of_set[team_one] == score_to_win or self.match.curr_score_of_set[team_two] == score_to_win:
                is_set_completed = True
            else: 
                if self.service_flag==1:
                    self.set_service_to_team()
                print(self.get_teams[team_one].is_have_service)
                score_one = self.match.curr_score_of_set[team_one]; score_two=self.match.curr_score_of_set[team_two]
                self.match.curr_score_of_set[team_one], self.match.curr_score_of_set[team_two] = self.calc_points(score_one, score_two)
                print(f"Points after each serve: {team_one}: {self.match.curr_score_of_set[team_one]} \t {team_two}: {self.match.curr_score_of_set[team_two]}")
            self.service_flag*=-1

    def set_service_to_team(self):
            team_have_service = next(self.pool)
            self.get_teams[team_have_service].is_have_service = True
            self.get_teams[next(self.pool)].is_have_service = False
            nxt = next(self.pool)

    def update_teams_scores_details(self):
        match_scorecard = self.match.get_match_scorecard
        first_team, second_team = match_scorecard[0]
        match_scorecard = [list(map(str,list(score))) for score in match_scorecard[1:]]
        for scores in match_scorecard:
            self.get_teams[first_team].score = "-".join(scores)
            self.get_teams[second_team].score = "-".join(scores[::-1])


    def display_match_winner(self):

        msg = "--"*10
        print(f"\n{msg}Match Result{msg}")
        table_data = utils.create_tabular_data(self.match.get_match_scorecard, self.match.num_of_sets_in_match)
        utils.disply_table(table_data)
        print(f"{msg}{msg}{msg}")

        winner_team = self.match.winner_team_name
        names_of_players_in_team = self._teams[winner_team].players
        names_of_players_in_team = " And ".join(names_of_players_in_team)
        print(f"\n*** Match won by team : {winner_team}")
        print(f"*** Players in {winner_team} : {names_of_players_in_team} ")
        print(f"*** Match won by score: {self._teams[winner_team].score} ")


    def update_match_winner_details(self):
        teams = self.team_names
        team_one, team_two = teams[0], teams[1]
        winner = None
        if self.get_teams[team_one].num_of_sets_won > self.get_teams[team_two].num_of_sets_won:
            winner = team_one
        else:
            winner = team_two
        self.get_teams[winner].won = True
        self.match.is_match_over = True
        self.match.winner_team_name = winner
        self.game_completed = True

    def check_winner_of_sets(self, score_one, score_two):
        if score_one>score_two:
            return 0
        else:
            return 1

    def check_if_any_team_won_majority_of_sets(self, first_team_sets_won, second_team_sets_won, num_of_sets_to_win_match):
        if first_team_sets_won>=num_of_sets_to_win_match or second_team_sets_won>=num_of_sets_to_win_match:
            return True
        else:
            return False

    def update_teams_sets_win_details(self, sets_won_by_teams):
        for team in sets_won_by_teams:
            self.get_teams[team].num_of_sets_won = sets_won_by_teams[team]

    def display_sets_winner(self, team_one, team_two):
        if self.match.curr_score_of_set[team_one] > self.match.curr_score_of_set[team_two]:
            winner = team_one
            result = (self.match.curr_score_of_set[team_one], self.match.curr_score_of_set[team_two])
        else:
            winner = team_two
            result = (self.match.curr_score_of_set[team_two], self.match.curr_score_of_set[team_one])    
        print(f"\n** Team {winner} has won set with points {result} **")

    def check_if_deuce_exists(self, team_one, team_two):
        deuce_score = self.match.deuce_score
        if self.match.curr_score_of_set[team_one] == deuce_score and self.match.curr_score_of_set[team_two] == deuce_score:
            return True
        return False

    def handle_deuce_score_condition(self, team_one, team_two):
        max_score = self.match.max_score
        while True:
            if abs(self.match.curr_score_of_set[team_one]-self.match.curr_score_of_set[team_two])==2:
                print("")
                break
            elif (self.match.curr_score_of_set[team_one]==max_score or self.match.curr_score_of_set[team_two]==max_score):
                break
            if self.service_flag==1:
                self.set_service_to_team()
            self.service_flag*=-1
            self.match.curr_score_of_set[team_one], self.match.curr_score_of_set[team_two] = self.calc_points(self.match.curr_score_of_set[team_one], self.match.curr_score_of_set[team_two])
            print(f"Points after each serve: {team_one}: {self.match.curr_score_of_set[team_one]} \t {team_two}: {self.match.curr_score_of_set[team_two]}")


    def calc_points(self, score_one, score_two):
        point = self.serve.serve()
        if point==0:
            score_one+=1
        else:
            score_two+=1
        return score_one, score_two


