from algorithm import *
import tkinter as tk
from tkinter import messagebox

current_chr = "x"

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

buttons = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]


class TicTacToe:

    def __init__(self):
        reset_board(board)
        global buttons

        self.root = tk.Tk()
        self.root.withdraw()
        self.root.resizable(False, False)
        self.root.title("Tic Tac Toe")
        self.play_area = tk.Frame(self.root, width=300, height=300, bg='white')

        self.menu_screen = tk.Toplevel()
        self.menu_screen.resizable(False, False)
        self.menu_screen.configure(width=300,
                                   height=250)
        self.message_screen = tk.Label(self.menu_screen, text="Choose mode: ", font="Sans")
        self.message_screen.place(relheight=0.15, relx=0.25, rely=0.1)

        self.vs_ai = tk.Button(self.menu_screen, text="VS AI", font="Sans",
                               command=lambda: self.configure_players(True))
        self.vs_opponent = tk.Button(self.menu_screen, text="VS OPPONENT", font="Sans",
                                     command=lambda: self.configure_players(False))

        self.vs_ai.place(relheight=0.3, relwidth=0.5, relx=0.25, rely=0.25)
        self.vs_opponent.place(relheight=0.3, relwidth=0.5, relx=0.25, rely=0.55)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.menu_screen.protocol("WM_DELETE_WINDOW", self.on_closing_menu)
        self.root.wait_window()

    def on_closing(self):
        self.root.quit()
        self.root.destroy()
        quit()

    def on_closing_menu(self):
        self.menu_screen.destroy()
        self.root.quit()
        self.root.destroy()
        quit()

    def configure_players(self, param):
        global current_chr
        current_chr = 'x'
        self.menu_screen.destroy()
        self.root.deiconify()
        for x in range(3):
            for y in range(3):
                buttons[x][y] = ButtonGrid(x, y, self.play_area, self.root, param)

        self.play_area.pack(pady=10, padx=10)


class ButtonGrid:

    def __init__(self, x, y, play_area, root, param):
        global b
        self.play_area = play_area
        self.root = root
        self.x = x
        self.y = y
        self.occupied = None
        if not param:
            self.button = tk.Button(self.play_area, text="", width=10, height=5, command=self.set_vs_opponent)
        else:
            self.button = tk.Button(self.play_area, text="", width=10, height=5, command=self.set_vs_ai)
        self.button.grid(row=x, column=y)

    def set_vs_opponent(self):
        global current_chr
        if not self.occupied:
            self.button.configure(text=current_chr, bg='snow', fg='black')
            board[self.x][self.y] = current_chr
            game_result = check_current_state(board)
            if game_result == -10:
                self.message_box = messagebox.showinfo("WIN!", "X WON!")
                self.root.destroy()
                TicTacToe()
            elif game_result == 10:
                self.message_box = messagebox.showinfo("WIN!", "O WON!")
                self.root.destroy()
                TicTacToe()
            self.occupied = current_chr
            if current_chr == "x":
                current_chr = "o"
            elif current_chr == "o":
                current_chr = "x"
            if not check_moves_left(board):
                self.message_box = messagebox.showinfo("TIE", "TIE!")
                self.root.destroy()
                TicTacToe()

    def set_vs_ai(self):
        global current_chr
        current_chr = 'x'
        if not self.occupied:
            self.button.configure(text=current_chr, bg='snow', fg='black')
            self.occupied = current_chr
            board[self.x][self.y] = current_chr
            if not check_moves_left(board):
                self.message_box = messagebox.showinfo("TIE", "TIE!")
                self.root.destroy()
                TicTacToe()
            best_move = find_best_move(board)
            buttons[best_move[0]][best_move[1]].set_ai()
            board[best_move[0]][best_move[1]] = 'o'
            game_result = check_current_state(board)
            if game_result == -10:
                self.message_box = messagebox.showinfo("WIN!", "X WON!")
                self.root.destroy()
                TicTacToe()
            elif game_result == 10:
                self.message_box = messagebox.showinfo("WIN!", "O WON!")
                self.root.destroy()
                TicTacToe()

    def set_ai(self):
        self.button.configure(text='o', bg='snow', fg='black')
        self.occupied = 'o'
