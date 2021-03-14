#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codigos.Cards import *
from application.welcome_frame import *
from application.board_frame import *
from application.casos_especiais import *
import numpy as np
import time
from tkinter import *
import tkinter as tk

class Application(Cards, Welcome, Board_Frame, Especiais):
    def __init__(self, root):
        root.title('Perfil')
        self.mainframe = tk.Frame(root, height='12c', width='30c', bg='#f26d14') # orange
        self.mainframe.grid(column=1, row=1, columnspan=10, rowspan=10)
        Cards.__init__(self)
        Welcome.__init__(self)
        Board_Frame.__init__(self)
        Especiais.__init__(self)
        self.welcome()

    def game(self):
        """
        
        Set the game frame
        """
        self.reset_mount()
        # left side with the questions, id, hint 
        self.left_side_game()
        # right side with the board
        self.right_side_game()
        self.vez_de_quem = np.random.randint(0, self.num_players, 1)[0]
        self.next_card()
        self.func_next_player()
    
    def to_dict(self, items):
        output = dict()
        for i in range(len(items)):
            output[i+1] = items[i]
            output[i+1]['command'] = lambda i=i: self.choosen_question(i+1)
        return output
    
    def choosen_question(self, id_button):
        self.button_20_questions[id_button]['bg'] = '#dd1717'
        self.button_20_questions[id_button]['state'] = DISABLED
        self.label_round_hint['text'] = 'Pergunta {0}\n{1}'.format(id_button, self.card[str(id_button)])
        self.pontos_rodada -= 1
        self.casos_exepcionais(self.card[str(id_button)])
        
        # root.wait_variable(self._guess)
    
    def chute(self):
        if self._guess.get().upper() == self.card['resposta'].upper() or self.pontos_rodada == 0:
            self.att_points(self.vez_de_quem)
            self.mostrar_resposta()
            self.reset_questions()
            self.next_card()
            # outras consequencias, óbvio
        self._guess.set('')
        self.label_round_hint['text'] = ''
        self.func_next_player()
            
    def att_labels_rodada(self):
        self.label_rodada.config(text = self.rodada)
        self.label_id_card.config(text = self.card['id'])
        self.label_dica.config(text = self.card['dica'])
    
    def reset_questions(self):
        for question in self.button_20_questions.values():
            question['bg'] = '#eae8e8'
            question['state'] = NORMAL
        
        if self.pontuacao.max() >= 120 or len(self.mount_cards) <= 0:
            self.end_game()
    
    def end_tudo(self):
        root.after(5000, root.destroy())
    
    def att_points(self, pos):
        self.pontuacao[pos] += self.pontos_rodada
        self.att_label_pontuacao()
    
    def att_label_pontuacao(self):
        for pos in range(len(self.players_frame)):
            self.players_frame[pos].winfo_children()[1]['text'] = self.pontuacao[pos]
        
    def func_next_player(self):
        self.players_frame[self.vez_de_quem].winfo_children()[0]['bg'] = '#eae8e8'
        self.vez_de_quem = (self.vez_de_quem + 1) % self.num_players
        self.players_frame[self.vez_de_quem].winfo_children()[0]['bg'] = '#b9ba05'
    
    def end_game(self):
        time.sleep(5)
        root.destroy()
    