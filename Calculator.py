import tkinter as tk

# Create a function to update the expression
def button_click(number):
    current = expression.get()
    expression.set(current + str(number))

# Create a function to clear the display
def clear():
    expression.set("")

# Create a function to calculate the result
def calculate():
    try:
        result = str(eval(expression.get()))
        expression.set(result)
    except:
        expression.set("Error")

# Create the main application window
app = tk.Tk()
app.title("Calculator")

# Create a StringVar to hold the expression
expression = tk.StringVar()
expression.set("")

# Create an entry widget to display the expression
entry = tk.Entry(app, textvariable=expression, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

# Create the calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        tk.Button(app, text=button, padx=20, pady=20, command=clear).grid(row=row_val, column=col_val)
    elif button == '=':
        tk.Button(app, text=button, padx=20, pady=20, command=calculate).grid(row=row_val, column=col_val)
    else:
        tk.Button(app, text=button, padx=20, pady=20, command=lambda num=button: button_click(num)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the application
app.mainloop()
