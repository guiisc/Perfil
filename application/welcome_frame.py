#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codigos.Cards import *
import numpy as np
from tkinter import *
import tkinter as tk

class Welcome:
    def __init__(self):
        pass
    
    def welcome(self):
        """
        
        Set welcome Frame
        """
        self.frame_begin = tk.Frame(self.mainframe, bg='#2d2b2b') # gray
        self.frame_begin.place(relx=.1, rely=.1, relheight=.8, relwidth=.8)
        greeting = tk.Label(self.frame_begin, text='Welcome to Perfil', bg='#9033df', fg='#000000', font=('Arial', 16))
        greeting.place(relx=.3, rely=.13 , relheight=.15, relwidth=.4)
        which_entry = tk.Label(self.frame_begin, text='Number of Players', font=('Arial', 12))
        which_entry.place(relx=.3, rely=.3 , relheight=.07, relwidth=.4)
        
        self.n_players = StringVar()
        num_players_entry = tk.Entry(self.frame_begin, textvariable=self.n_players, justify=CENTER)
        num_players_entry.place(relx=.4, rely=.45 , relheight=.08, relwidth=.1)
        self.button_begin = tk.Button(self.frame_begin, text='Ok', command= lambda i = which_entry, j=num_players_entry: self.get_num_players(i,j))
        self.button_begin.place(relx=.55, rely=.45, relheight=.08, relwidth=.05)
    
    def get_num_players(self, which_entry, entry):
        """
        
        Get the number of players
        """
        try:
            self.num_players = int(self.n_players.get())
            self.pontuacao = np.repeat(0, self.num_players)
            which_entry['text'] = 'Player 1'
            self.get_players(which_entry, entry)
        except ValueError:
            pass
    
    def get_players(self, which_entry, entry):
        """
        
        Get the name of the players
        """
        def name_player(event):
            players_name.append(entry.get())
            which_entry['text'] = 'Player ' + str(len(players_name) + 1)
            if len(players_name) == self.num_players:
                self.players = np.array(players_name)
                self.frame_begin.destroy()
                self.game()
        
        players_name = []
        self.button_begin.bind('<Button-1>', name_player)
