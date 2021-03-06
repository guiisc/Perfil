import numpy as np

class Dealer:
    def __init__(self):
        pass
    
    def first_dealer(self):
        self.dealer = np.random.randint(0, self.num_players, 1)[0]
        self.vez_de_quem = (self.dealer + 1) % self.num_players
    
    def next_dealer(self):
        self.dealer = (self.dealer + 1) % self.num_players
        self.vez_de_quem = (self.dealer + 1) % self.num_players