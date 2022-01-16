


class InvalidMatchTypeException(Exception):
    def __init__(self, message="This Match Type is invalid"):
        self.message = message
        super().__init__(self.message)

class InvalidPlayersNameException(Exception):
    def __init__(self, message="Player names provied is invalid"):
        self.message = message
        super().__init__(self.message)


class MatchIsAlreadyOverException(Exception):
    def __init__(self, message="Match is already over"):
        self.message = message
        super().__init__(self.message)

class MatchSetsEvenException(Exception):
    def __init__(self, message="Match sets count must be odd"):
        self.message = message
        super().__init__(self.message)

class NumberNegativeException(Exception):
    def __init__(self, message="Match sets count must be odd"):
        self.message = message
        super().__init__(self.message)