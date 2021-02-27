from tkinter import *
import tkinter as tk

class Application():
    def __init__(self, root):
        root.title('Perfil')
        mainframe = tk.Frame(root, height='12c', width='30c', bg='#f26d14') # orange
        mainframe.grid(column=1, row=1, columnspan=10, rowspan=10)

        # left side with the questions, id, hint 
        frame1 = tk.Frame(mainframe, bg='#48f214') # lime green
        frame1.place(relheight=1, relwidth=.5)
        rodada_label = tk.Label(frame1, text='Rodada {0}'.format('self.rodada'), padx=5, pady=0)
        rodada_label.place(relx=.15, rely=.05, relwidth=0.7)
        id_question_label = tk.Label(frame1, text='ID: {0}'.format('self.card[\'id\']'), padx=5)
        id_question_label.place(relx=.15, rely=.12, relwidth=0.3)
        dica_question_label = tk.Label(frame1, text='DICA: {0}'.format('self.card[\'dica\']'), padx=5)
        dica_question_label.place(relx=.55, rely=0.12, relwidth=0.3)

        opcoes_frame = tk.Frame(frame1, relief=RAISED, bg='black')
        opcoes_frame.place(relx=.2, rely=.2, relheight=.4, relwidth=0.6)

        opcoes_perguntas = []
        for linha in range(4):
            for coluna in range(5):
                opcoes_perguntas.append(tk.Button(opcoes_frame, text='{0}'.format(len(opcoes_perguntas)+1), padx=5, pady=5))
                opcoes_perguntas[-1].place(relx=coluna/5 + .05, rely=linha/4 + .05, relheight=.15 ,relwidth=.1)

        perguntas_frame = tk.Frame(frame1, height=mainframe['height']/3, width=mainframe['width']/2, bg='#fc18fc') # pink
        perguntas_frame.place(relx=.15, rely=.65, relheight=.3, relwidth=.7)
        pergunta = tk.Label(perguntas_frame, text='Pergunta {0}\n{1}'.format('self.num_question', 'question'))
        pergunta.place(relx=.1, rely=.05, relheight=.55, relwidth=.8)

        resposta = tk.Entry(perguntas_frame, text='Chute')
        resposta.place(relx=.1, rely=.65, relheight=.3, relwidth=.8)

        # right side with the board
        board = tk.Frame(mainframe, bg='#539edf') # light blue
        board.place(relx=0.5, rely=0, relheight=1, relwidth=.5)
        

root = Tk()
app = Application(root)
root.mainloop()
