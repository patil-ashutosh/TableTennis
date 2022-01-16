
from service.GameService import Game
from models.Match import MatchType



def play_doubles_game():
    game = Game()
    game.create_team("TeamA", ("Ashutosh", "Prashant"), match_type=MatchType.doubles.name)
    game.create_team("TeamB", ("Sujit", "Suraj"), match_type=MatchType.doubles.name)
    game.play_match()

def play_singles_game():
    game = Game()
    game.create_team("Team-A", "Ashutosh")
    game.create_team("Team-B", "Prashant")
    game.play_match()

if __name__ == "__main__":
    play_singles_game()