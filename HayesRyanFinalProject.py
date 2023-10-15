#Ryan Hayes
#Number Guessing Game GUI
#Program provides a basic GUI for a game start menu that can be easily adjusted for different games


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import subprocess  # Import the subprocess module for launching the game

# Global variables for background images
main_menu_bg_photo = None
options_menu_bg_photo = None

def create_main_menu():
    # Clear the main frame
    for widget in main_frame.winfo_children():
        widget.destroy()
    
    global main_menu_bg_photo  # Declare the global variable
    
    # Load background image for the main menu
    script_directory = os.path.dirname(os.path.abspath(__file__))
    main_menu_bg_path = os.path.join(script_directory, "images", "main_menu_background.png")
    
    try:
        main_menu_bg_image = Image.open(main_menu_bg_path)
        # Resize the image to fit the window size
        main_menu_bg_image = main_menu_bg_image.resize((initial_width, initial_height))
        main_menu_bg_photo = ImageTk.PhotoImage(main_menu_bg_image)
    except Exception as e:
        print(f"Error loading main menu background image: {e}")
        return

    # Set the background image for the main menu
    main_menu_bg_label = tk.Label(main_frame, image=main_menu_bg_photo)
    main_menu_bg_label.place(relwidth=1, relheight=1)

    # Center the Welcome label
    welcome_label = tk.Label(main_frame, text="Welcome to the Number Guessing Game!", font=("Helvetica", 16))
    welcome_label.place(relx=0.5, rely=0.4, anchor="center")

    # Buttons on the main menu
    start_button = tk.Button(main_frame, text="Start Game", command=start_game)
    options_button = tk.Button(main_frame, text="Options", command=open_options_menu)
    quit_button = tk.Button(main_frame, text="Quit", command=root.destroy)

    # Position the buttons using grid or pack
    start_button.place(relx=0.5, rely=0.5, anchor="center")
    options_button.place(relx=0.5, rely=0.6, anchor="center")
    quit_button.place(relx=0.5, rely=0.7, anchor="center")

def start_game():
    # Hide the main window
    root.withdraw()

    try:
        # Launch the game script as a separate process
        subprocess.run(["python", "game_script.py"], check=True)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error starting the game: {e}")

    # Show the main window again after the game exits (optional)
    root.deiconify()

def open_options_menu():
    # Replace this with the code to open the options menu
    create_options_menu()

def create_options_menu():
    # Clear the main frame
    for widget in main_frame.winfo_children():
        widget.destroy()

    global options_menu_bg_photo  # Declare the global variable
    
    # Load background image for the options menu
    script_directory = os.path.dirname(os.path.abspath(__file__))
    options_menu_bg_path = os.path.join(script_directory, "images", "options_menu_background.png")
    
    try:
        options_menu_bg_image = Image.open(options_menu_bg_path)
        # Resize the image to fit the window size
        options_menu_bg_image = options_menu_bg_image.resize((initial_width, initial_height))
        options_menu_bg_photo = ImageTk.PhotoImage(options_menu_bg_image)
    except Exception as e:
        print(f"Error loading options menu background image: {e}")
        return
    
    # Set the background image for the options menu
    options_menu_bg_label = tk.Label(main_frame, image=options_menu_bg_photo)
    options_menu_bg_label.place(relwidth=1, relheight=1)

    # Buttons on the options menu
    graphics_button = tk.Button(main_frame, text="Graphics", command=open_graphics_menu)
    audio_button = tk.Button(main_frame, text="Audio", command=open_audio_menu)
    accessibility_button = tk.Button(main_frame, text="Accessibility", command=open_accessibility_menu)
    back_button = tk.Button(main_frame, text="Back to Main Menu", command=create_main_menu)

    # Position the buttons using grid or pack
    graphics_button.place(relx=0.5, rely=0.4, anchor="center")
    audio_button.place(relx=0.5, rely=0.5, anchor="center")
    accessibility_button.place(relx=0.5, rely=0.6, anchor="center")
    back_button.place(relx=0.5, rely=0.9, anchor="center")

def open_graphics_menu():
    # Replace this with the code to open the graphics settings menu
    messagebox.showinfo("Graphics", "Graphics settings opened")

def open_audio_menu():
    # Replace this with the code to open the audio settings menu
    messagebox.showinfo("Audio", "Audio settings opened")

def open_accessibility_menu():
    # Replace this with the code to open the accessibility settings menu
    messagebox.showinfo("Accessibility", "Accessibility settings opened")

# Create the main window
root = tk.Tk()
root.title("Game Menu")

# Get the screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the initial window size (approximately half the screen dimensions)
initial_width = screen_width // 2
initial_height = screen_height // 2

# Calculate the x and y positions to center the window
x_position = (screen_width - initial_width) // 2
y_position = (screen_height - initial_height) // 2

# Set the window size and position
root.geometry(f"{initial_width}x{initial_height}+{x_position}+{y_position}")

# Configure row and column weights
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Main Menu Frame
main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, sticky="nsew")

# Create the main menu
create_main_menu()

# Main loop
root.mainloop()
