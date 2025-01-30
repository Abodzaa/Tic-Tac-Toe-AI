import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Tic-Tac-Toe")

player_x = 'X'
player_o = 'O'
empty_cell = ''

buttons = [[None, None, None] for _ in range(3)]

def on_click(row, col):
    if buttons[row][col]['text'] == empty_cell and not check_winner():
        buttons[row][col]['text'] = player_x
        if not check_winner():
            computer_move()

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != empty_cell:
            announce_winner(buttons[i][0]['text'])
            return True

        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != empty_cell:
            announce_winner(buttons[0][i]['text'])
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != empty_cell:
        announce_winner(buttons[0][0]['text'])
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != empty_cell:
        announce_winner(buttons[0][2]['text'])
        return True

    for row in buttons:
        for button in row:
            if button['text'] == empty_cell:
                return False

    announce_winner("It's a draw!")
    return True

def announce_winner(winner):
    if winner != "It's a draw!":
        messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
    else:
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")

def computer_move():
    best_score = -float('inf')
    best_move = None

    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] == empty_cell:
                buttons[row][col]['text'] = player_o
                score = bfs(board=buttons, depth=0, is_maximizing_player=False)
                buttons[row][col]['text'] = empty_cell

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    if best_move:
        row, col = best_move
        buttons[row][col]['text'] = player_o
        check_winner()

def bfs(board, depth, is_maximizing_player):
    result = evaluate(board)
    if result is not None:
        return result

    if is_maximizing_player:
        max_eval = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col]['text'] == empty_cell:
                    board[row][col]['text'] = player_o
                    eval = bfs(board, depth + 1, False)
                    board[row][col]['text'] = empty_cell
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col]['text'] == empty_cell:
                    board[row][col]['text'] = player_x
                    eval = bfs(board, depth + 1, True)
                    board[row][col]['text'] = empty_cell
                    min_eval = min(min_eval, eval)
        return min_eval

def evaluate(board):
    for i in range(3):
        if board[i][0]['text'] == board[i][1]['text'] == board[i][2]['text'] != empty_cell:
            if board[i][0]['text'] == player_o:
                return 1
            else:
                return -1

        if board[0][i]['text'] == board[1][i]['text'] == board[2][i]['text'] != empty_cell:
            if board[0][i]['text'] == player_o:
                return 1
            else:
                return -1

    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != empty_cell:
        if board[0][0]['text'] == player_o:
            return 1
        else:
            return -1

    if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != empty_cell:
        if board[0][2]['text'] == player_o:
            return 1
        else:
            return -1

    for row in board:
        for button in row:
            if button['text'] == empty_cell:
                return None

    return 0  # It's a draw

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text=empty_cell, font=('normal', 40), width=3, height=1,
                                      command=lambda row=row, col=col: on_click(row, col))
        buttons[row][col].grid(row=row, column=col)

root.mainloop()
