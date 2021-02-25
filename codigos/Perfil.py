import numpy as np
import pandas as pd
import json
import sys
from codigos.Cards import *
from codigos.Players import *
from codigos.Board import *
from codigos.Rodada import *
from codigos.Dealer import *


class Perfil(Cards, Players, Board, Rodada, Dealer):
    def __init__(self):
        Cards.__init__(self)
        Players.__init__(self)
        Board.__init__(self)
        Rodada.__init__(self)
        Dealer.__init__(self)
        pass
    
    def initializate_partida(self):
        """
        Define the player's username and setting the mount of cards
        """
        self.partida_ativa = True
        Players.getting_players(self)
        Cards.reset_mount(self)
        Dealer.first_dealer(self, self.num_players)
        self.vez_de_quem = (self.dealer+1) % self.num_players
        Board.setting_board(self)
        return
    
    def new_game(self):
        """
        
        New Game ?
        """
        while True:
            resposta = input('Novo jogo ? \n[Y/N]:').upper()
            if resposta == 'Y':
#                 Nova partida
                return
            elif resposta == 'N':
                self.partida_ativa = False
                return
#                 Encerrar
    
    def end_game_cards(self):
        """
        
        End  Game, start another one ?
        """
        print('Jogo acabou Galera')
        self.new_game()
    
    def end_game_winner(self, player):
        """
        
        End  Game and someone won
        """
        print(self.players[player], 'ganhou, os outros são muito ruins.\nPelo amor')
        self.new_game()
    
    def proxima_rodada(self, dealer):
        """
        
        Verficiar se o jogo acabou seja por falta de cartas ou pontuação
        Caso contrário puxar a próxima carta e começar a rodada
        """
        if len(self.mount_cards) <= 0: self.end_game_cards()
        elif self.pontuacao.max() >= self.board_tot: self.end_game_winner(self.pontuacao.argmax())
        self.next_card()
        return self.initialize_rodada()
    
    def print_final_rodada(self):
        print('\n',  100*'-', sep='')
        print('Dealer:', self.players[self.dealer])
        for player, pts in zip(self.players, self.pontuacao):
            print(player, 'tem', pts, 'pontos')
        print(100*'-')
    
    def partida(self):
        """
        
        Aqui será controlada a partida como um todo
        """
        self.initializate_partida()
        while self.partida_ativa:
            self.print_final_rodada()
            player, pontos = self.proxima_rodada(self.dealer)
            self.pontuacao[player] += 20 - pontos
            self.pontuacao[self.dealer] += pontos
            self.print_final_rodada()
            self.next_dealer()
        pass

    