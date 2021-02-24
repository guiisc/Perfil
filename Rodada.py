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
            self.next_question()
            if input('Chute:') == self.card['resposta']:
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
            question = input('Number of the question:')
            if not question.isnumeric(): continue
            if question in self.questions:
                print('Escolhe outra')
            elif 0 < int(question) and int(question) <= 20:
                self.questions.append(question)
                print('Pergunta {0}:'.format(question), self.card[question])
                return