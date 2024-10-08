import tkinter as tk

# Functions for the buttons
def greet():
    label.config(text="Hello, welcome!")

def clear():
    label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Dark Theme Tkinter App")
root.geometry("300x200")

# Set dark background color
root.config(bg="#2e2e2e")

# Create a label
label = tk.Label(root, text="Press a button", font=("Arial", 16), fg="white", bg="#2e2e2e")
label.pack(pady=20)

# Create buttons
greet_button = tk.Button(root, text="Greet", command=greet, font=("Arial", 14), bg="#3e3e3e", fg="white", width=10)
greet_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=clear, font=("Arial", 14), bg="#3e3e3e", fg="white", width=10)
clear_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
