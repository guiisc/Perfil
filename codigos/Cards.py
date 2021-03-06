import numpy as np
import os
import sys
import json

class Cards:
    def __init__(self):
        pass
    
    def reset_mount(self):
        path = os.path.realpath('..')
        self.mount_cards = json.load(open(path+'\Perfil\perguntas.json'), encoding='None')
        self.rodada = 0
    
    def next_card(self):
        """
        
        Get next card in the mount
        """
        self.rodada += 1
        while True:
            carta = self.mount_cards.pop(np.random.randint(0, len(self.mount_cards), 1)[0])
            if np.random.random(1) >= 0.85:
                pos_palpite = np.random.randint(1, 20, 1)[0]
                carta['{0}'.format(pos_palpite)] = 'Escolha alguém para avançar 2 casas'
            if np.random.random(1) >= 0.85:
                pos_palpite = np.random.randint(1, 20, 1)[0]
                carta['{0}'.format(pos_palpite)] = 'Escolha alguém para recuar 3 casas'
            if np.random.random(1) >= 0.65:
                pos_perde_vez = np.random.randint(1, 20, 1)[0]
                carta['{0}'.format(pos_perde_vez)] = 'Perde a vez'
            
            self.card = carta
            self.id = carta['id']
            self.dica = carta['dica']
            self.att_labels()
            self.pontos_rodada = 20
            self.next_dealer()
            return