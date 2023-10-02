#Ryan Hayes
#Video Game Menu Screen UI Project
#Program provides a basic video game UI that can be modified to fit different games

import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring

# Callback functions
def start_game():
    player_name = askstring("Player Name", "Enter Your Name:")
    if player_name:
        messagebox.showinfo("Game Started", f"Welcome, {player_name}!")
    else:
        messagebox.showerror("Error", "Please enter your name.")

def options():
    # Implement the options menu or other actions here
    messagebox.showinfo("Options", "Options menu will be implemented soon!")

def exit_game():
    answer = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if answer:
        root.quit()

# Create the main window
root = tk.Tk()
root.title("Game Menu")

# Labels
welcome_label = tk.Label(root, text="Welcome to My Game", font=("Helvetica", 16))
version_label = tk.Label(root, text="Version 1.0")

# Buttons
start_button = tk.Button(root, text="Start Game", command=start_game)
options_button = tk.Button(root, text="Options", command=options)
exit_button = tk.Button(root, text="Exit", command=exit_game)

# Place widgets using grid layout
welcome_label.grid(row=0, column=0, columnspan=2, pady=10)
start_button.grid(row=1, column=0, pady=10)
options_button.grid(row=1, column=1, pady=10)
exit_button.grid(row=2, column=0, columnspan=2, pady=10)
version_label.grid(row=3, column=0, columnspan=2)

# Main loop
root.mainloop()
