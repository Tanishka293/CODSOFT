import tkinter as tk

def click(button):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def on_enter(e, button):
    button['background'] = 'lightblue'

def on_leave(e, button, original_color):
    button['background'] = original_color

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry widget
entry = tk.Entry(root, width=16, font=('Arial', 28), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Create button widgets
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

button_colors = {
    '/': 'orange',
    '*': 'orange',
    '-': 'orange',
    '+': 'orange',
    '=': 'green',
    'C': 'red',
    'B': 'blue'
}

row_val = 1
col_val = 0

for button in buttons:
    color = button_colors.get(button, 'SystemButtonFace')
    btn = tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), bg=color, command=lambda b=button: click(b) if b != '=' else calculate())
    btn.grid(row=row_val, column=col_val)
    btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b))
    btn.bind("<Leave>", lambda e, b=btn, c=color: on_leave(e, b, c))
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Create clear button
clear_button = tk.Button(root, text='C', width=5, height=2, font=('Arial', 18), bg='red', command=clear)
clear_button.grid(row=row_val, column=col_val)
clear_button.bind("<Enter>", lambda e, b=clear_button: on_enter(e, b))
clear_button.bind("<Leave>", lambda e, b=clear_button, c='red': on_leave(e, b, c))

# Create backspace button
back_button = tk.Button(root, text='Back', width=5, height=2, font=('Arial', 18), bg='blue', command=backspace)
back_button.grid(row=row_val, column=col_val + 1)
back_button.bind("<Enter>", lambda e, b=back_button: on_enter(e, b))
back_button.bind("<Leave>", lambda e, b=back_button, c='blue': on_leave(e, b, c))

# Start the main event loop
root.mainloop()