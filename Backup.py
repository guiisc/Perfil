import numpy as np
import pandas as pd
import json

class Cards:
    def __init__(self):
        pass
    
    def reset_mount(self):
        self.mount_cards = json.load(open('perguntas.json'))
    
    def next_card(self):
        """
        
        Get next card in the mount
        """
        carta = self.mount_cards.pop(np.random.randint(0, len(self.mount_cards), 1)[0])
        if np.random.random(1) >= 0.95:
            pos_palpite = np.random.randint(1, 20, 1)[0]
            carta['{0}'.format(pos_palpite)] = 'Palpite a qualquer hora'
        if np.random.random(1) >= 0.65:
            pos_perde_vez = np.random.randint(1, 20, 1)[0]
            carta['{0}'.format(pos_perde_vez)] = 'Perde a vez'
        
        self.card = carta
        self.id = carta['id']
        self.dica = carta['dica']

class Board:
    def __init__(self):
        pass
    
    def setting_board(self):
        """
        
        Setting total length of the board
        """
        self.board_tot = 121#int(input('Tamanho do tabuleiro'))
    

class Dealer:
    def __init__(self):
        pass
    
    def first_dealer(self, num_players):
        self.num_players = num_players
        self.dealer = np.random.randint(0, self.num_players, 1)[0]
    
    def next_dealer(self):
        self.dealer = self.dealer % self.num_players
    
    
class Players:
    def __init__(self):
        return
        
    def getting_players(self):
        """
        
        Define how many players, and their usernames
        """
        players = []
        self.num_players = int(input('Number of players'))
        for i in range(self.num_players):
            players.append(input('Player {0}'.format(i+1)))
        self.players = np.array(players)
    
    def next_player(self, dealer, vez_de_quem):
        """
        
        Define whose turn it is
        """
        if vez_de_quem + 1 == dealer:
            vez_de_quem += 2
        else:
            vez_de_quem += 1
        return vez_de_quem % self.num_players
    
class Rodada():
    def __init__(self):
        pass
    
    def initialize_rodada(self, dealer, num_players, card):
        self.dealer = dealer
        self.num_players = num_players
        self.card = card
        self.questions = []
        pass
    
    def core_rodada(self):
        while len(self.questions) <= 20:
            print(self.vez_de_quem, 'ist dran')
            self.next_question()
            if input('Chute') == self.card['resposta']:
#             Acertou
                return True
            self.vez_de_quem = Players.next_player(self.dealer, self.vez_de_quem)
#         Errou
        return False

    def next_question(self):
        """
        
        Escolhe e mostra a próxima pergunta
        """
        question = input('Question')
        if question in self.questions:
            print('Escolhe outra')
        else: 
            self.questions.append(question)
            print(self.card[question])
    
    
    
class Partida(Cards, Players, Board, Rodada, Dealer):
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
        Players.getting_players(self)
        Cards.reset_mount(self)
        Dealer.first_dealer(self, self.num_players)
        self.vez_de_quem = (self.dealer+1) % self.num_players
        return
    
    def proxima_rodada(self, dealer):
        if len(self.mount_cards) <= 0:
            print('Jogo acabou Galera')
            raise TypeError("Acabou o Jogo")
        self.next_card()
        self.initialize_rodada(dealer=dealer, num_players=self.num_players, card=self.card)
        print('dentro da Partida', self.vez_de_quem)
        

        