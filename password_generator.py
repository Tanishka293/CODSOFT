import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, complexity):
    if not (1 <= complexity <= 10):
        raise ValueError("Complexity must be between 1 and 10")

    # Define character sets for different complexity levels
    char_sets = [
        string.ascii_lowercase,  # Level 1-2: Lowercase letters
        string.ascii_uppercase,  # Level 3-4: Uppercase letters
        string.digits,           # Level 5-6: Digits
        string.punctuation       # Level 7-10: Special characters
    ]
    
    # Select character sets based on complexity
    selected_characters = char_sets[0]  # Start with lowercase letters
    
    if complexity >= 3:
        selected_characters += char_sets[1]  # Add uppercase letters
    if complexity >= 5:
        selected_characters += char_sets[2]  # Add digits
    if complexity >= 7:
        selected_characters += char_sets[3]  # Add special characters

    # Generate the password
    password = ''.join(random.choice(selected_characters) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(length_entry.get())
        complexity = int(complexity_entry.get())
        if length <= 0:
            raise ValueError("Password length must be greater than 0")
        password = generate_password(length, complexity)
        result_label.config(text="GENERATE PASSWORD: " + password)
        copy_button.config(state=tk.NORMAL)
    except ValueError as e:
        messagebox.showerror("Invalid Input!!", str(e))

def on_copy():
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text").split(": ")[1])
    messagebox.showinfo("COPIED!", "Password copied to clipboard")

def on_enter(e):
    e.widget['background'] = '#b3b3b3'

def on_leave(e):
    e.widget['background'] = '#f0f0f0'

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")  # Set the window size

# Set the background color
root.configure(bg='#d9d9d9')

# Create and place the length label and entry
length_label = tk.Label(root, text="PASSWORD LENGTH:", bg='#d9d9d9')
length_label.pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Create and place the complexity label and entry
complexity_label = tk.Label(root, text="PASSWORD COMPLEXITY (1-10):", bg='#d9d9d9')
complexity_label.pack(pady=5)
complexity_entry = tk.Entry(root)
complexity_entry.pack(pady=5)

# Create and place the generate button
generate_button = tk.Button(root, text="GENERATE PASSWORD", command=on_generate, bg='#f0f0f0')
generate_button.pack(pady=10)
generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)

# Create and place the result label
result_label = tk.Label(root, text="", bg='#d9d9d9')
result_label.pack(pady=5)

# Create and place the copy button
copy_button = tk.Button(root, text="COPY TO CLIPBOARD", command=on_copy, state=tk.DISABLED, bg='#f0f0f0')
copy_button.pack(pady=5)
copy_button.bind("<Enter>", on_enter)
copy_button.bind("<Leave>", on_leave)

# Run the main loop
root.mainloop()