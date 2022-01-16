from abc import abstractmethod

class Player:
    def __init__(self, name):
        self.names = name

    @abstractmethod
    def set_name():
        pass

    @property
    def players_names(self):
        return self.names


class SinglesPlayer(Player):
    def __init__(self, names):
        self.set_name(names)

    def set_name(self, name1):
        self.names = [name1]

class DoublesPlayer(Player):
    def __init__(self, name1, name2):
        self.set_name(name1, name2)

    def set_name(self, name1, name2):
        self.names = [name1, name2]
