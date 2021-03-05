from codigos.Perfil import *
import numpy as np
from tkinter import *
import tkinter as tk

class Application(Perfil):
    def __init__(self, root):
        root.title('Perfil')
        self.mainframe = tk.Frame(root, height='12c', width='30c', bg='#f26d14') # orange
        self.mainframe.grid(column=1, row=1, columnspan=10, rowspan=10)
        Perfil.__init__(self)
        self.begin()
    
    def begin(self):
        # begin_background = tk.Image(open('bg.jpeg'))
        self.begin_frame = tk.Frame(self.mainframe, bg='#000000')
        self.begin_frame.place(relx=.1, rely=.1, relheight=.8, relwidth=.8)
        greeting = tk.Label(self.begin_frame, text='Welcome to Perfil', bg='#9033df')
        greeting.place(relx=.3, rely=.13 , relheight=.15, relwidth=.4)
        which_entry = tk.Label(self.begin_frame, text='Number of Players')
        which_entry.place(relx=.3, rely=.3 , relheight=.07, relwidth=.4)
        
        self.n_players = StringVar()
        num_players_entry = tk.Entry(self.begin_frame, textvariable=self.n_players, justify=CENTER)
        num_players_entry.place(relx=.4, rely=.45 , relheight=.08, relwidth=.1)
        self.ok_button = tk.Button(self.begin_frame, text='Ok', command= lambda i = which_entry, j=num_players_entry: self.get_num_players(i,j))
        self.ok_button.place(relx=.55, rely=.45, relheight=.08, relwidth=.05)
        
    def get_num_players(self, which_entry, entry):
        try:
            self.num_players = int(self.n_players.get())
            self.pontuacao = np.repeat(0, self.num_players)
            which_entry['text'] = 'Player 1'
            self.get_players(which_entry, entry)
        except ValueError:
            pass
    
    def get_players(self, which_entry, entry):
        def name_player(event):
            players_name.append(entry.get())
            which_entry['text'] = 'Player ' + str(len(players_name) + 1)
            if len(players_name) == self.num_players:
                self.players = np.array(players_name)
                self.begin_frame.destroy()
                self.game()
        
        players_name = []
        self.ok_button.bind('<Button-1>', name_player)

    def game(self):
        self.reset_mount()
        self.next_card()
        # left side with the questions, id, hint 
        self.left_side_game()
        # right side with the board
        self.right_side_game()
    
    def left_side_game(self):
        frame1 = tk.Frame(self.mainframe, bg='#48f214') # lime green
        frame1.place(relheight=1, relwidth=.5)
        rodada_label = tk.Label(frame1, text='Rodada {0}'.format(self.rodada), padx=5, pady=0)
        rodada_label.place(relx=.15, rely=.05, relwidth=0.7)
        id_question_label = tk.Label(frame1, text='ID: {0}'.format(self.card['id']), padx=5)
        id_question_label.place(relx=.15, rely=.12, relwidth=0.3)
        dica_question_label = tk.Label(frame1, text='DICA: {0}'.format(self.card['dica']), padx=5)
        dica_question_label.place(relx=.55, rely=0.12, relwidth=0.3)
        
        self.question_frame(frame1)
        self.guess_frame(frame1)
        
    def guess_frame(self, frame1):
        perguntas_frame = tk.Frame(frame1, bg='#fc18fc') # pink
        perguntas_frame.place(relx=.15, rely=.65, relheight=.3, relwidth=.7)
        self.pergunta = tk.Label(perguntas_frame, text='Pergunta None \n None', wraplength=250)
        self.pergunta.place(relx=.1, rely=.05, relheight=.55, relwidth=.8)
        
        _chute = tk.StringVar(perguntas_frame)
        resposta = tk.Entry(perguntas_frame, justify=CENTER, textvariable=_chute)
        resposta.place(relx=.1, rely=.65, relheight=.3, relwidth=.55)
        guess_button = tk.Button(perguntas_frame, text='Guess', command= lambda i=_chute.get(): self.chute(i))
        guess_button.place(relx=.7, rely=.65, relheight=.3, relwidth=.2)
    
    def question_frame(self, frame1):
        opcoes_frame = tk.Frame(frame1, relief=RAISED, bg='black')
        opcoes_frame.place(relx=.2, rely=.2, relheight=.4, relwidth=0.6)
        
        opcoes_perguntas = []
        for linha in range(4):
            for coluna in range(5):
                opcoes_perguntas.append(tk.Button(opcoes_frame, text='{0}'.format(len(opcoes_perguntas)+1), padx=5, pady=5))
                opcoes_perguntas[-1].place(relx=coluna/5 + .05, rely=linha/4 + .05, relheight=.15 ,relwidth=.1)
        self.opcoes_perguntas = self.to_dict(opcoes_perguntas)
    
    def right_side_game(self):
        board = tk.Frame(self.mainframe, bg='#539edf') # light blue
        board.place(relx=0.5, rely=0, relheight=1, relwidth=.5)
        
        players_frame = []
        for coluna in range(self.num_players):
            players_frame.append(tk.Frame(board))
            players_frame[-1].place(relx=.05 + coluna*(1-0.01*self.num_players)/self.num_players, rely=.1, relheight=.2, relwidth=(.9-0.05*self.num_players)/self.num_players)
            tk.Label(players_frame[-1], text=self.players[coluna]).place(relx=0, rely=0, relheight=.5, relwidth=1)
            tk.Label(players_frame[-1], text=self.pontuacao[coluna], bg='#787878').place(relx=0, rely=.5, relheight=.5, relwidth=1)
    
    
    def to_dict(self, items):
        output = dict()
        for i in range(len(items)):
            output[i+1] = items[i]
            output[i+1]['command'] = lambda i=i: self.choosen_question(i+1)
        return output
    
    def choosen_question(self, id_button):
        self.opcoes_perguntas[id_button]['bg'] = '#dd1717'
        self.opcoes_perguntas[id_button]['state'] = DISABLED
        self.pergunta['text'] = 'Pergunta {0}\n{1}'.format(id_button, self.card[str(id_button)])
#         new_question()
    
    def chute(self, chute):
        self.pontuacao[0] += 10
        if chute.upper() == self.card['resposta'].upper():
            self.reset_questions()
            self.next_card()
            # outras consequencias, óbvio
            # contar pontos
            # mudar a vez de quem é
        
    
    def reset_questions(self):
        for question in self.opcoes_perguntas.values():
            # question['bg'] = '#dd1717'
            question['state'] = NORMAL
    
    def end_tudo(self):
        root.after(5000, root.destroy())

root = Tk()
app = Application(root)
root.mainloop()