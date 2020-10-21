from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, h):
        self.h = h
        pass

    @abstractmethod
    def cloth_exp(self):
        pass


class Coat(Clothes):
    @property
    def cloth_exp(self):
        return self.h / (6.5 + 0.5)


class Suit(Clothes):
    @property
    def cloth_exp(self):
        return 2 * self.h + 0.3


coat = Coat(42)
suit = Suit(1.8)
print(coat.cloth_exp)
print(suit.cloth_exp)
