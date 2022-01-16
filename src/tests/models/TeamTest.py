import unittest

from models.Team import Team
from models.Match import MatchType


class TeamTest(unittest.TestCase):
    def test_get_team_name(self):
        team_name = "Mumbai_Team"
        team = Team(team_name)
        self.assertEqual(team.name, team_name)

    def test_add_players_to_team(self):
        team_name = "Mumbai_Team"
        players_name = "ashutosh"
        match_type = MatchType.singles.name

        team = Team(team_name)
        team.add_players_to_team(match_type, players_name)
        self.assertEqual(team.players, [players_name])
