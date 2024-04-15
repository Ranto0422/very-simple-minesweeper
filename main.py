import tkinter as tk
import random

class Minesweeper():
    def __init__(self, ismine=False):
        self.root = tk.Tk()
        
        self.isopen = False
        self.ismine = ismine
        self.board = [[0] * cols for _ in range(rows)]  # 0 represents an empty cell
        self.place_mines
        # Window Size
        self.root.geometry("350x500")
        self.root.resizable(False, False)
        # Title Widget
        self.root.title('Mines')
        self.label = tk.Label(self.root, text="Enter number of Creepers to spawn", font = ('Arial', 10))
        self.label.pack(padx = 15, pady = 10)

        # Entry Widget
        self.entry = tk.Entry(self.root)
        self.entry.pack(padx = 10, pady = 10)
        
        # Button Widget
        self.button = tk.Button(self.root, text = "Start", font = ('Arial', 18))
        self.button.pack(padx = 10, pady = 10)
        
        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.pack(padx=10, pady=10)
        
        for i in range(5):
            for j in range(5):
                btn = tk.Button(self.buttonframe, text='', width=7, height=3,
                                command=lambda row=i, col=j: self.on_button_click(row, col))
                btn.grid(row=i, column=j, sticky=tk.W+tk.E+tk.N+tk.S)
        
        
        def on_button_click(self):
            if self.board[row][col] == -1:
                self.game_over()
            else:
                self.reveal_cell(row, col)
        
        def reveal_cell(self, row, col):
            self.cell_btn_object.configure(text='opened')
        def place_mines(self):
            mines = random.sample(range(5 * 5), self.ismine)
            for mine in mines:
                row = mine // 5
                col = mine % 5
                self.board[row][col] = -1
                
        self.root.mainloop()
Minesweeper()