import enum
from exceptions import exceptions


class MatchType(enum.Enum):
    singles = 1
    doubles = 2

class Match:
    def __init__(self, match_type, num_of_sets, score_to_win, max_score):
        self._num_of_sets = self._is_valid_sets_count(num_of_sets)
        self._score_to_win = self._is_valid_number(score_to_win)
        self._deuce_score = score_to_win-1
        self._max_score = self._is_valid_number(max_score)
        self._max_tie_scor = max_score-1
        self._sets = []
        self._num_of_sets_to_win_match = (num_of_sets//2)+1
        self._is_match_over = False
        self._winner_team_name = None
        self._curr_set = 1
        self._curr_score_of_set = {}

    # get count of number sets in match
    @property
    def num_of_sets_in_match(self):
        return self._num_of_sets

    def _is_valid_sets_count(self, num_of_sets):
        if num_of_sets%2 ==0 or num_of_sets<0:
            raise exceptions.MatchSetsEvenException()
        return num_of_sets

    def _is_valid_number(self, num):
        if num<=0:
            raise exceptions.NumberNegativeException("score must be positive")
        return num

    @property
    def score_to_win_set(self):
        return self._score_to_win

    @property
    def max_score(self):
        return self._max_score

    @property
    def deuce_score(self):
        return self._deuce_score

    @property
    def get_match_scorecard(self):
        return self._sets

    @property
    def num_of_sets_to_win_match(self):
        return self._num_of_sets_to_win_match

    @property
    def is_match_over(self):
        return self._is_match_over

    @is_match_over.setter
    def is_match_over(self, is_match_over):
        self._is_match_over = is_match_over

    @property
    def winner_team_name(self):
        return self._winner_team_name

    @winner_team_name.setter
    def winner_team_name(self, winner_team_name):
        self._winner_team_name = winner_team_name

    @property
    def curr_score_of_set(self):
        return self._curr_score_of_set

    @curr_score_of_set.setter
    def curr_score_of_set(self, key, val):
        self._curr_score_of_set[key] = val

    def reset_curr_score_of_set(self):
        for key in self.curr_score_of_set:
            self.curr_score_of_set[key] = 0
        
    def update_match_scorecard(self, score):
        self._sets.append(score)



