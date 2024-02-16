import tkinter as tk
from tkinter import messagebox

def display_board():
    for row in range(3):
        for col in range(3):
            button = tk.Button(root, text=board[row][col], font=('Arial', 24), width=6, height=3,
                               command=lambda r=row, c=col: on_click(r, c))
            button.grid(row=row, column=col)

def check_win(player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def is_draw():
    return all(cell != ' ' for row in board for cell in row)

def on_click(row, col):
    global turn

    if board[row][col] == ' ':
        board[row][col] = players[turn % 2]
        display_board()

        if check_win(players[turn % 2]):
            messagebox.showinfo("Game Over", f"Player {players[turn % 2]} wins!")
            root.quit()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            root.quit()

        turn += 1

# Initialize GUI
root = tk.Tk()

root.title("Tic-Tac-Toe")

# Initialize game variables
board = [[' ' for _ in range(3)] for _ in range(3)]
players = ['X', 'O']
turn = 0

# Display initial board
display_board()

root.mainloop()
