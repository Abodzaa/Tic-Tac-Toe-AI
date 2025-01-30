import tkinter as tk
from tkinter import messagebox
import random

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Define the variables for players
player_x = 'X'
player_o = 'O'
empty_cell = ''

# Create a 3x3 grid for the game
buttons = [[None, None, None] for _ in range(3)]

# Function to handle button clicks
def on_click(row, col):
    if buttons[row][col]['text'] == empty_cell and not check_winner():
        buttons[row][col]['text'] = player_x
        if not check_winner():
            computer_move()

# Function to check for a win or a draw
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

# Function to announce the winner or draw
def announce_winner(winner):
    if winner != "It's a draw!":
        messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
    else:
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")

# Function to handle computer's move (DFS-based)
def computer_move():
    best_score = -float('inf')
    best_move = None

    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] == empty_cell:
                buttons[row][col]['text'] = player_o
                score = dfs(board=buttons, depth=0, is_maximizing_player=False)
                buttons[row][col]['text'] = empty_cell

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    if best_move:
        row, col = best_move
        buttons[row][col]['text'] = player_o
        check_winner()

# Depth-First Search (DFS) algorithm
def dfs(board, depth, is_maximizing_player):
    result = evaluate(board)
    if result is not None:
        return result

    if is_maximizing_player:
        max_eval = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col]['text'] == empty_cell:
                    board[row][col]['text'] = player_o
                    eval = dfs(board, depth + 1, False)
                    board[row][col]['text'] = empty_cell
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col]['text'] == empty_cell:
                    board[row][col]['text'] = player_x
                    eval = dfs(board, depth + 1, True)
                    board[row][col]['text'] = empty_cell
                    min_eval = min(min_eval, eval)
        return min_eval

# Evaluation function to determine game state
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

# Create and configure the buttons
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text=empty_cell, font=('normal', 40), width=3, height=1,
                                      command=lambda row=row, col=col: on_click(row, col))
        buttons[row][col].grid(row=row, column=col)

# Start the game
if random.choice([True, False]):
    # Computer starts the game
    computer_move()

# Start the main event loop
root.mainloop()
#//////////////////////////////////////////////////////
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
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import tkinter as tk
from tkinter import messagebox
import random

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Define the variables for players
player_x = 'X'
player_o = 'O'
empty_cell = ''

# Create a 3x3 grid for the game
buttons = [[None, None, None] for _ in range(3)]

# Variable to track the current player
current_player = player_x

# Function to handle button clicks
def on_click(row, col):
    if buttons[row][col]['text'] == empty_cell and not check_winner():
        buttons[row][col]['text'] = current_player
        if not check_winner():
            switch_player()
            computer_move()

# Function to check for a win or a draw
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

# Function to announce the winner or draw
def announce_winner(winner):
    if winner != "It's a draw!":
        messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
    else:
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")

# Function to switch to the other player
def switch_player():
    global current_player
    if current_player == player_x:
        current_player = player_o
    else:
        current_player = player_x

# Function to handle computer's move
def computer_move():
    if not check_winner():
        if current_player == player_o:
            best_score = -float('inf')
            best_move = None

            for row in range(3):
                for col in range(3):
                    if buttons[row][col]['text'] == empty_cell:
                        buttons[row][col]['text'] = player_o
                        score = minimax(board=buttons, depth=2, is_maximizing_player=False)
                        buttons[row][col]['text'] = empty_cell

                        if score > best_score:
                            best_score = score
                            best_move = (row, col)

            if best_move:
                row, col = best_move
                buttons[row][col]['text'] = player_o
                if not check_winner():
                    switch_player()

# Minimax algorithm for computer's move
def minimax(board, depth, is_maximizing_player):
    result = evaluate(board)
    if depth == 0 or result is not None:
        return result

    if is_maximizing_player:
        max_eval = -float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col]['text'] == empty_cell:
                    board[row][col]['text'] = player_o
                    eval = minimax(board, depth - 1, False)
                    board[row][col]['text'] = empty_cell
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(3):
            for col in range(3):
                if board[row][col]['text'] == empty_cell:
                    board[row][col]['text'] = player_x
                    eval = minimax(board, depth - 1, True)
                    board[row][col]['text'] = empty_cell
                    min_eval = min(min_eval, eval)
        return min_eval

# Evaluation function to determine game state
def evaluate(board):
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != empty_cell:
            if buttons[i][0]['text'] == player_o:
                return 1
            else:
                return -1

        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != empty_cell:
            if buttons[0][i]['text'] == player_o:
                return 1
            else:
                return -1

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != empty_cell:
        if buttons[0][0]['text'] == player_o:
            return 1
        else:
            return -1

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != empty_cell:
        if buttons[0][2]['text'] == player_o:
            return 1
        else:
            return -1

    for row in board:
        for button in row:
            if button['text'] == empty_cell:
                return None

    return 0  # It's a draw

# Create and configure the buttons
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text=empty_cell, font=('normal', 40), width=3, height=1,
                                      command=lambda row=row, col=col: on_click(row, col))
        buttons[row][col].grid(row=row, column=col)

# Start the game
if random.choice([True, False]):
    # Computer starts the game
    computer_move()

# Start the main event loop
root.mainloop()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
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
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
import tkinter as tk
from tkinter import messagebox
import random
import queue as Q

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Define the variables for players
player_x = 'X'
player_o = 'O'
empty_cell = ''

# Create a 3x3 grid for the game
buttons = [[None, None, None] for _ in range(3)]

# Create a priority queue for UCS
ucs_queue = Q.PriorityQueue()

# Function to handle button clicks
def on_click(row, col):
    if buttons[row][col]['text'] == empty_cell and not check_winner():
        buttons[row][col]['text'] = player_x
        if not check_winner():
            computer_move()

# Function to check for a win or a draw
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

# Function to announce the winner or draw
def announce_winner(winner):
    if winner != "It's a draw!":
        messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
    else:
        messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")

# Function to handle computer's move (UCS-based)
def computer_move():
    if not check_winner():
        best_move = ucs_search()
        if best_move:
            row, col = best_move
            buttons[row][col]['text'] = player_o
            check_winner()

# UCS search function
def ucs_search():
    # Represent the board as a string
    current_state = ''.join([button['text'] for row in buttons for button in row])
    ucs_queue.put((0, current_state, None))

    while not ucs_queue.empty():
        cost, state, move = ucs_queue.get()

        if check_winner():
            return move

        next_player = player_o if state.count(player_x) > state.count(player_o) else player_x

        for i in range(3):
            for j in range(3):
                if i * 3 + j < len(state) and state[i * 3 + j] == empty_cell:
                    new_state = list(state)
                    new_state[i * 3 + j] = next_player
                    ucs_queue.put((cost + 1, ''.join(new_state), (i, j)))

    return None

# Create and configure the buttons
for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text=empty_cell, font=('normal', 40), width=3, height=1,
                                      command=lambda row=row, col=col: on_click(row, col))
        buttons[row][col].grid(row=row, column=col)

# Start the game
if random.choice([True, False]):
    # Computer starts the game
    computer_move()

# Start the main event loop
root.mainloop()
