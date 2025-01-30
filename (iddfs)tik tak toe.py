import tkinter as tk
import random
import copy

# Initialize the Tic-Tac-Toe board
board = [" " for _ in range(9)]

# Initialize player and AI symbols
player_symbol = "X"
ai_symbol = "O"

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons for the Tic-Tac-Toe board
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", font=("Helvetica", 16), width=4, height=2,
                       command=lambda i=i: on_click(i))
    buttons.append(button)
    button.grid(row=i // 3, column=i % 3)

# Function to handle player's move
def on_click(index):
    if board[index] == " ":
        make_move(index, player_symbol)
        check_game_over()
        make_ai_move()

# Function to make a move
def make_move(index, symbol):
    board[index] = symbol
    buttons[index].config(text=symbol)
    buttons[index].config(state="disabled")

# Function to check if the game is over
def check_game_over():
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] != " ":
            buttons[a].config(bg="green")
            buttons[b].config(bg="green")
            buttons[c].config(bg="green")
            disable_buttons()
            return True
    if " " not in board:
        disable_buttons()
        return True
    return False

# Function to disable all buttons
def disable_buttons():
    for button in buttons:
        button.config(state="disabled")

# Iterative Deepening Depth-First Search (IDDFS)
def iddfs(board, depth, is_maximizing_player):
    if depth == 0 or check_game_over():
        if player_wins():
            return -1
        elif ai_wins():
            return 1
        return 0

    if is_maximizing_player:
        max_eval = -float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = ai_symbol
                eval = iddfs(board, depth - 1, False)
                board[i] = " "
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(9):
            if board[i] == " ":
                board[i] = player_symbol
                eval = iddfs(board, depth - 1, True)
                board[i] = " "
                min_eval = min(min_eval, eval)
        return min_eval

# Function to make AI's move
def make_ai_move():
    if " " in board:
        best_move = -1
        best_eval = -float("inf")
        for i in range(9):
            if board[i] == " ":
                temp_board = copy.deepcopy(board)
                temp_board[i] = ai_symbol
                eval = iddfs(temp_board, 9, False)
                if eval > best_eval:
                    best_eval = eval
                    best_move = i
        make_move(best_move, ai_symbol)
        check_game_over()

# Function to check if the player has won
def player_wins():
    return check_winner(player_symbol)

# Function to check if the AI has won
def ai_wins():
    return check_winner(ai_symbol)

# Function to check if a symbol has won
def check_winner(symbol):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] == symbol:
            return True
    return False

# Start the game
if random.choice([True, False]):
    make_ai_move()

root.mainloop()
