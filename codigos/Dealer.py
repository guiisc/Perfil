import numpy as np
import pandas as pd
import json


class Dealer:
    def __init__(self):
        pass
    
    def first_dealer(self, num_players):
        self.num_players = num_players
        self.dealer = np.random.randint(0, self.num_players, 1)[0]
    
    def next_dealer(self):
        self.dealer = (self.dealer + 1) % self.num_players
        self.vez_de_quem = (self.dealer + 1) % self.num_players