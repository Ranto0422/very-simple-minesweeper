import random
import tkinter as tk
from tkinter import messagebox


class MinesweeperGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Minesweeper")
        self.root.resizable(0, 0)
        self.size = 5
        self.num_bombs = 0
        self.game_grid = None
        self.buttons = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.points = 0
        
        # Load da images
        self.stationary_image = tk.PhotoImage(file="python.png")
        self.stationary_image=self.stationary_image.subsample(2, 2)
        self.pressed_image = tk.PhotoImage(file="diamond.png")
        self.pressed_image=self.pressed_image.subsample(4, 4)
        self.bomb_image = tk.PhotoImage(file="boom.png")
        self.bomb_image=self.bomb_image.subsample(4, 4)
        
        self.create_widgets()

    def create_widgets(self):
        top_frame = tk.Frame(self.root)
        top_frame.pack(side=tk.TOP, fill=tk.X)

        self.label = tk.Label(top_frame, text="Enter number of Mines", font=('Skia', 10, 'bold'))
        self.label.pack()

        self.button = tk.Button(top_frame, text="Start Game", command=self.start_game)

        self.entry = tk.Entry(top_frame)
        self.entry.pack()

        # Load the image and create a smaller version
        self.start_button = tk.PhotoImage(file='start.png')
        self.smaller_image = self.start_button.subsample(4, 4)

        # Create the button with the smaller image
        self.initialize = tk.Button(self.root, image=self.smaller_image, command=self.start_game)
        self.initialize.pack(pady=10)

        self.points_label = tk.Label(top_frame, text=f"Points: {self.points}")  # Display points
        self.points_label.pack()

        # grid of bottom
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(expand=True, fill=tk.BOTH)

        # Create and show the grid initially (disabled)
        self.show_grid(disabled=True)
    def start_game(self):
        try:
            self.num_bombs = int(self.entry.get())
            if self.num_bombs >= self.size * self.size:
                messagebox.showerror("Error", "Too many bombs! Please choose a smaller number.")
                return

            self.game_grid = create_grid(self.size, self.num_bombs)
            self.show_grid(disabled=False)  # Enable the buttons
            self.points = 0  # Reset points for a new game
            self.update_points_display()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def show_grid(self, disabled=False):
        # Clear grid frame
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        self.root.geometry("350x500")

        for row in range(self.size):
            for col in range(self.size):
                button = tk.Button(
                    self.grid_frame,
                    image=self.stationary_image,
                    command=lambda r=row, c=col: self.click_cell(r, c),
                    state=tk.DISABLED if disabled else tk.NORMAL,  # Disable initially
                )
                button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
                self.buttons[row][col] = button

        # uniform size grid and column
        for i in range(self.size):
            self.grid_frame.grid_rowconfigure(i, weight=1, minsize=70)
            self.grid_frame.grid_columnconfigure(i, weight=1, minsize=70)

    def click_cell(self, row, col):
        if self.game_grid[row][col] == 'B':
            self.reveal_grid()  # Reveal all cells first
            self.root.update_idletasks()  # Update the GUI to show the revealed cells
            messagebox.showinfo("Game Over", f"Boom! You hit a bomb. Game over! \n Total points: {self.points}")
            self.show_grid(disabled=True)  # Disable the buttons after game over
            self.root.wait_window(self.root)  # Wait for the messagebox to be closed
            self.start_game()  # Restart the game
        else:
            self.buttons[row][col].config(image=self.pressed_image)
            self.points += 10  # Increase points for each safe cell clicked
            self.update_points_display()

    def update_points_display(self):
        self.points_label.config(text=f"Points: {self.points}")

    def reveal_grid(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.game_grid[row][col] == 'B':
                    self.buttons[row][col].config(image=self.bomb_image)
                else:
                    self.buttons[row][col].config(image=self.pressed_image)


def create_grid(size, num_bombs):
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    bomb_positions = random.sample(range(size * size), num_bombs)

    for pos in bomb_positions:
        row, col = divmod(pos, size)
        grid[row][col] = 'B'

    return grid


if __name__ == "__main__":
    root = tk.Tk()
    app = MinesweeperGUI(root)
    root.mainloop()

