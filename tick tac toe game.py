import tkinter as tk 
player1 = input("Enter name of player 1: ") 
player2 = input("Enter name of player 2: ") 

current_player = "X"

x_color = "#f591b5"  
o_color = "#52c2c1"  

bg_color = "#4b005f"  
from tkinter import messagebox 

def winner(): 
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8],#combo is a loop variable 
                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                 [0, 4, 8], [2, 4, 6]]: 
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "": #TO check if all buttons contain same symbol
            for i in combo:
                buttons[i].config(bg="green") #change background color to green
                winner_name = player1 if buttons[combo[0]]["text"] == "X" else player2 # to print the winner's name
                loser_name = player2 if winner_name == player1 else player1
           
            messagebox.showinfo("Game Over", f"Player {winner_name} wins!\n{loser_name} loses!") #display a message box with the winner's name")
            for button in buttons:
                button.config(state="disabled") #disable loop so no one can play after winning
            return True
    return False  

def tie():
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Game Over", "It's a tie!")
        for button in buttons:
            button.config(state="disabled")
        return True
    return False  

def button_click(i): #defines what happens when a button is clicked
    if buttons[i]["text"] == "":  
        buttons[i]["text"] = current_player 
        if current_player == "X":
            buttons[i].config(fg=x_color) #displays 'X' in the cell
        else:
            buttons[i].config(fg=o_color) #displays 'o' in the cell
        if winner(): #asks to stop if winner found (function recall)
            return
        if tie():  #to check tie
            return
        toggle_player() #function recall


def toggle_player(): #to switch bw players
    global current_player 
    current_player = "O" if current_player == "X" else "X" #toggle between players
    name = player1 if current_player == "X" else player2 #display name of the current player
    label.config(text=f"Player {name}'s turn") #update the label to show current player's turn

root = tk.Tk() #create a window
root.title("Tic-Tac-Toe") #set title  
root.config(bg=bg_color)           

buttons = [tk.Button(root, text="", font=("Arial", 20),
                      width=5, height=2, bg=bg_color, 
                      command=lambda i=i: button_click(i)) #tells Tkinter what to execute when a button is clicked
                      for i in range(9)] #create buttons for the game

for i, button in enumerate(buttons): #place buttons in a grid
    button.grid(row=i//3, column=i%3)

current_player = "X"
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("Arial", 14)) #create a label to show current player's turn
label.grid(row=3, column=0, columnspan=3) #place the label in the grid
root.mainloop() #start the loop