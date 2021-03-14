#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from tkinter import *
import tkinter as tk

class Especiais:
    def __init__(self):
        pass
    
    def func_frame_escolhidos(self):
        self.frame_especiais = tk.Frame(self.mainframe, bg='#ff0000') # Red
        
        self.label_especiais = tk.Label(self.frame_especiais, bg='#ffa500') # Orange
        self.label_especiais.place(relx = 0.1, rely = 0.05, relheight = 0.3, relwidth = 0.8)
        
        self.player_especiais = tk.StringVar()
        self.entry_especiais = tk.Entry(self.frame_especiais, textvariable=self.player_especiais, justify=CENTER)
        self.entry_especiais.place(relx = 0.1, rely = 0.4, relheight = 0.3, relwidth = 0.8)
        
        self.button_ok_especiais = tk.Button(self.frame_especiais, text='OK')
        self.button_ok_especiais.place(relx = 0.1, rely = 0.75, relheight = 0.2, relwidth = 0.8)
    
    def player_escolhido(self, pts):
        """
        Verificar se o player escolhido não é quem escolheu, e modificar a pontuação
        """
        pos = (self.players==self.player_especiais.get()).argmax()
        if pos != self.vez_de_quem and self.player_especiais.get() in self.players:
            print('foi')
            self.pontuacao[pos] =  np.maximum(self.pontuacao[pos] + pts, 0)
            self.att_label_pontuacao()
            self.frame_especiais.destroy()
            return
        else:
            print('não foi')
        
    def casos_exepcionais(self, caso):
        """
        
        Quando cai em 'perde a vez', avance 2 casas, escolha alguém para voltar 3 casas
        """
        if caso == 'Perde a vez':
            self.func_next_player()
            return
            
        self.func_frame_escolhidos()
        if caso == 'Escolha alguém para avançar 2 casas':
            self.label_especiais['text'] = 'Escolha alguém para avançar 2 casas'
            self.frame_especiais.place(relheight=1, relwidth=.5)
            self.button_ok_especiais['command'] = lambda i = 2: self.player_escolhido(i)
        elif caso == 'Escolha alguém para recuar 3 casas':
            self.label_especiais['text'] = 'Escolha alguém para recuar 3 casas'
            self.frame_especiais.place(relheight=1, relwidth=.5)
            self.button_ok_especiais['command'] = lambda i = -3: self.player_escolhido(i)
        return