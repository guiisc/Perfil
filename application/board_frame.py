#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codigos.Cards import *
import numpy as np
from tkinter import *
import tkinter as tk

class Board_Frame:
    def __init__(self):
        pass
    
    def left_side_game(self):
        """
        
        Set the top left side of the game grame
        """
        frame_left_side = tk.Frame(self.mainframe, bg='#48f214') # lime green
        frame_left_side.place(relheight=1, relwidth=.5)
        self.label_rodada = tk.Label(frame_left_side, text=None, padx=5, pady=0)
        self.label_rodada.place(relx=.15, rely=.05, relwidth=0.7)
        self.label_id_card = tk.Label(frame_left_side, text=None, padx=5)
        self.label_id_card.place(relx=.15, rely=.12, relwidth=0.3)
        self.label_dica = tk.Label(frame_left_side, text=None, padx=5)
        self.label_dica.place(relx=.55, rely=0.12, relwidth=0.3)
        
        self.question_frame(frame_left_side)
        self.guess_frame(frame_left_side)
    
    def question_frame(self, frame_left_side):
        """
        
        Set the 20-button frame, and those buttons for each question
        """
        frame_20_questions = tk.Frame(frame_left_side, relief=RAISED, bg='black')
        frame_20_questions.place(relx=.2, rely=.2, relheight=.4, relwidth=0.6)
        
        button_20_questions = []
        for linha in range(4):
            for coluna in range(5):
                button_20_questions.append(tk.Button(frame_20_questions, text='{0}'.format(len(button_20_questions)+1), padx=5, pady=5))
                button_20_questions[-1].place(relx=coluna/5 + .05, rely=linha/4 + .05, relheight=.15 ,relwidth=.1)
        self.button_20_questions = self.to_dict(button_20_questions)
    
    def guess_frame(self, frame_left_side):
        frame_guess = tk.Frame(frame_left_side, bg='#fc18fc') # pink
        frame_guess.place(relx=.15, rely=.65, relheight=.3, relwidth=.7)
        self.label_round_hint = tk.Label(frame_guess, text='Pergunta None \n None', wraplength=250)
        self.label_round_hint.place(relx=.1, rely=.05, relheight=.55, relwidth=.8)
        
        self._guess = tk.StringVar(frame_guess)
        entry_guess = tk.Entry(frame_guess, justify=CENTER, textvariable=self._guess)
        entry_guess.place(relx=.1, rely=.65, relheight=.3, relwidth=.55)
        button_guess = tk.Button(frame_guess, text='Guess', command= lambda: self.chute())
        button_guess.place(relx=.7, rely=.65, relheight=.3, relwidth=.2)
    
    def right_side_game(self):
        frame_board = tk.Frame(self.mainframe, bg='#539edf') # light blue
        frame_board.place(relx=0.5, rely=0, relheight=1, relwidth=.5)
        
        self.players_frame = []
        for coluna in range(self.num_players):
            self.players_frame.append(tk.Frame(frame_board))
            self.players_frame[-1].place(relx=.05 + coluna*(1-0.01*self.num_players)/self.num_players, rely=.1, relheight=.2, relwidth=(.9-0.05*self.num_players)/self.num_players)
            tk.Label(self.players_frame[-1], text=self.players[coluna]).place(relx=0, rely=0, relheight=.5, relwidth=1)
            tk.Label(self.players_frame[-1], text=self.pontuacao[coluna], bg='#787878').place(relx=0, rely=.5, relheight=.5, relwidth=1)