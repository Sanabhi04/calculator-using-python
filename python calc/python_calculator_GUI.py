import tkinter as tk

# Function to update expression
def press(key):
    entry_text.set(entry_text.get() + str(key))

# Function to clear entry
def clear():
    entry_text.set("")

# Function to calculate result
def calculate():
    try:
        result = eval(entry_text.get())
        entry_text.set(result)
    except:
        entry_text.set("Error")

# Create window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

entry_text = tk.StringVar()

# Entry box
entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Button frame
frame = tk.Frame(root)
frame.pack()

# Buttons list
buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row = 0
col = 0

for btn in buttons:
    if btn == '=':
        tk.Button(frame, text=btn, width=7, height=2, command=calculate).grid(row=row, column=col)
    else:
        tk.Button(frame, text=btn, width=7, height=2, command=lambda x=btn: press(x)).grid(row=row, column=col)

    col += 1
    if col == 4:
        col = 0
        row += 1

# Clear button
tk.Button(root, text="Clear", width=30, height=2, command=clear).pack(pady=10)

root.mainloop()
