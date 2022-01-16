from models.Player import DoublesPlayer
from models.Player import SinglesPlayer
from exceptions import exceptions

class Team:
    def __init__(self, name):
        self._name = name
        self.players = None
        self._num_of_sets_won = 0 
        self._is_won = False
        self._score = []
        self.is_have_service = False

    def add_players_to_team(self, match_type, players_name):
        if match_type == "doubles":
            self.validate_match_type_doubles_parameters(players_name)
            player_one, player_two = players_name
            self.players = DoublesPlayer(player_one, player_two).players_names
        elif match_type == "singles":
            self.validate_match_type_singles_parameters(players_name)
            self.players = SinglesPlayer(players_name).players_names
        else:
            raise exceptions.InvalidMatchTypeException("Match Type: "+ match_type +" is invalid")

    def validate_match_type_doubles_parameters(self, players_name):
        if isinstance(players_name, list) or isinstance(players_name, tuple):
            if len(players_name)<2:
                msg = f"Players names :{players_name} is invalid, For doubles match 2 players must form team"
                raise exceptions.InvalidPlayersNameException(msg)
            player_one, player_two = players_name[0], players_name[1]
        else:
            msg = f"Players names :{players_name} is invalid, For doubles match 2 players must form team"

    def validate_match_type_singles_parameters(self, players_name):
        if isinstance(players_name, list) or isinstance(players_name, tuple):
            if len(players_name)<1:
                msg = f"Players names :{players_name} is invalid, For singles match 1 players must form team"
                raise exceptions.InvalidPlayersNameException(msg)
            players_name = players_name[0]
        else:
            if not players_name:
                raise exceptions.InvalidPlayersNameException(f"Players name: {players_name} cannot be empty")

    @property
    def name(self):
        return self._name

    @property
    def num_of_sets_won(self):
        return self._num_of_sets_won

    @num_of_sets_won.setter
    def num_of_sets_won(self, num_of_sets_won):
        self._num_of_sets_won = num_of_sets_won

    @property
    def is_have_service(self):
        return self._is_have_service

    @is_have_service.setter
    def is_have_service(self, is_service):
        self._is_have_service = is_service

    @property
    def won(self):
        return self._won

    @won.setter
    def won(self, is_win):
        self._won = is_win

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        return self._score.append(score)