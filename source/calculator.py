import tkinter as tk

# Function to update the display when a button is clicked
def button_click(number):
    current = entry.get()                           # get text from the entry box (input field)
    entry.delete(0, tk.END)                         # clear the entry box
    entry.insert(0, str(current) + str(number))     # add the previous text + the new number press to the entry box

# Function to clear the display
def clear_display():
    entry.delete(0, tk.END)                         # clear the entry box

# Function to delete the last character
def backspace():
    current = entry.get()                           # get text from the entry box (input field)
    entry.delete(len(current) - 1, tk.END)          # delete the last character of the entry box

# Function to toggle the sign of the number
def toggle_sign():
    current = entry.get()                           # get text from the entry box (input field)
    if current and current[0] == "-":               # check if first character is a "-" (minus sign)
        entry.delete(0)                             # toggle the minus sign
    else:
        entry.insert(0, "-")

# Function to perform arithmetic operation
def operate():
    try:
        result = eval(entry.get())                  # get text from the entry box and evaluate the expression
        entry.delete(0, tk.END)                     # clear the entry box
        entry.insert(0, str(result))                # display the result in entry box
    except:
        entry.delete(0, tk.END)                     # clear the entry box
        entry.insert(0, "Error")                    # display an "Error" message in entry box

# Create a Tkinter window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry widget to display the input and result
C_FONT = "Arial"
C_FONTSZ = 16
entry = tk.Entry(root, width=20, font=(C_FONT, C_FONTSZ), bd=5)
entry.grid(row=0, column=0, columnspan=4, ipady=10)

# Create buttons for numbers and operations
buttons = [
    ("7",   1, 0, 1), ("8", 1, 1, 1), ("9", 1, 2, 1), ("/", 1, 3, 1),   # number 7,8,9, divide
    ("4",   2, 0, 1), ("5", 2, 1, 1), ("6", 2, 2, 1), ("*", 2, 3, 1),   # number 4,5,6, multiply
    ("1",   3, 0, 1), ("2", 3, 1, 1), ("3", 3, 2, 1), ("-", 3, 3, 1),   # number 1,2,3, minus
    ("+/-", 4, 0, 1), ("0", 4, 1, 1), (".", 4, 2, 1), ("+", 4, 3, 1),   # negate, 0, dot, plus
    ("C",   5, 0, 1), ("←", 5, 1, 1), ("=", 5, 2, 2)                    # clear, backspace, equal
]


# Create and place the buttons in the grid
for (text, row, col, span) in buttons:
    if text == "←":  # Create a backspace button
        button = tk.Button(root, text=text, width=5*span, height=2, font=(C_FONT, C_FONTSZ),
                           command=backspace)
    elif text == "+/-":  # Create a toggle sign button
        button = tk.Button(root, text=text, width=5*span, height=2, font=(C_FONT, C_FONTSZ),
                           command=toggle_sign)
    elif text == "=":  # Create an equal button
        button = tk.Button(root, text=text, width=5*span, height=2, font=(C_FONT, C_FONTSZ), bd=0,
                           command=operate)
        #button.columnconfigure(2)
    elif text == "C":  # Create an Clear button
        button = tk.Button(root, text=text, width=5*span, height=2, font=(C_FONT, C_FONTSZ),
                           command=clear_display)
    else:
        button = tk.Button(root, text=text, width=5*span, height=2, font=(C_FONT, C_FONTSZ),
                           command=lambda text=text: button_click(text))
    button.grid(row=row, column=col, columnspan=span)

# Run the Tkinter event loop
root.mainloop()

