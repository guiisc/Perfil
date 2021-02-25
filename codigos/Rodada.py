import numpy as np
import pandas as pd
import json

class Rodada():
    def __init__(self):
        pass
    
    def initialize_rodada(self):
        self.questions = []
        return self.core_rodada()
    
    def core_rodada(self):
        """
        
        Controle de quem é a vez e quem acertou
        """
        while len(self.questions) <= 20:
            print('\n', self.players[self.vez_de_quem], ' ist dran', sep='')
            if not self.next_question(): continue
            chute = input("Chute: ").upper()
            if chute == self.card['resposta'].upper():
#             Acertou
                print("ACERTOU\n")
                return self.vez_de_quem, len(self.questions)
            print("NOPE")
            self.vez_de_quem = self.next_player(self.dealer, self.vez_de_quem)
        return self.dealer, len(self.questions)

    def next_question(self):
        """
        
        Escolhe e mostra a próxima pergunta
        """
        print("Perguntas já escolhidas:", sorted(list(map(int, self.questions))))
        while True:
            question = input('Number of the question: ')
            if not question.isnumeric(): continue
            if question in self.questions:
                print('Escolhe outra')
            elif 0 < int(question) and int(question) <= 20:
                self.questions.append(question)
                print('Pergunta {0}:'.format(question), self.card[question])
                if not self.casos_exepcionais(self.card[question]): return False
                return True
    
    def casos_exepcionais(self, caso):
        """
        
        Quando cai em 'perde a vez', avance 2 casas, escolha alguém para voltar 3 casas
        """
        if caso == 'Perde a vez':
            self.vez_de_quem = self.next_player(self.dealer, self.vez_de_quem)
            return False
        elif caso == 'Escolha alguém para avançar 2 casas':
            while True:
                player = input("escolha um entre {0}:\n".format(self.players))
                if not player in self.players: continue
                player = (self.players==player).argmax()
                if not player == self.vez_de_quem: continue # Não pode escolher a si mesmo
                self.pontuacao[player] += 2
                return True
        elif caso == 'Escolha alguém para recuar 3 casas':
            while True:
                player = input("escolha um entre {0}:\n".format(self.players))
                if not player in self.players: continue
                player = (self.players==player).argmax()
                self.pontuacao[player] = np.max(self.pontuacao[player] - 3, 0) # Não pode ficar negativo
                return True
        return True