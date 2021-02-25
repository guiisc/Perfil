import numpy as np
import pandas as pd
import json

class Players:
    def __init__(self):
        return
        
    def getting_players(self):
        """
        
        Define how many players, and their usernames
        """
        players = []
        self.num_players = int(input('Number of players: '))
        for i in range(self.num_players):
            players.append(input('Player {0}: '.format(i+1)))
        self.players = np.array(players)
        self.pontuacao = np.repeat(0, self.num_players)
    
    def next_player(self, dealer, vez_de_quem):
        """
        
        Define whose turn it is
        """
        if vez_de_quem + 1 == dealer:
            vez_de_quem += 2
        else:
            vez_de_quem += 1
        return vez_de_quem % self.num_players
    
    def update_pontuacao(self, player, pontuacao):
        """
        
        Controle da pontuação do jogo
        """
        self.pontuacao[player] += pontuacao