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
