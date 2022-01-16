import random
from abc import abstractmethod


class Serve:
    def __init__(self, minValue=1, maxValue=100):
        self.minValue = minValue
        self.maxValue = maxValue

    @abstractmethod
    def serve(self):
        pass


class RandomServe(Serve):
    def __init__(self, minValue=1, maxValue=100):
        super().__init__(minValue, maxValue) 

    def serve(self):
        return random.randint(self.minValue, self.maxValue)%2

class EvenServe(Serve):
    def __init__(self, minValue=1, maxValue=100):
        super().__init__(minValue, maxValue)

    def serve(self):
        return random.randrange(self.minValue+(self.minValue%2), self.maxValue+1, 2)%2

class OddServe(Serve):
    def __init__(self, minValue=1, maxValue=100):
        super().__init__(minValue, maxValue)

    def serve(self):
        if self.minValue % 2 == 0:
            self.minValue+=1
        return random.randrange(self.minValue, self.maxValue+1, 2)%2