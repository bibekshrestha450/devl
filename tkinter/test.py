# import tkinter as tk

# app = tk.Tk()
# app.geometry("500*500")

# username=tk.Label(app,text="username")
# username.pack()
# uname=tk.enter(app)
# username.pack()
# def say():
#     uname_val=uname.get()
#     print(f"hello {uname_val}")

# button=tk.Button(app,text="click me")
# root.mainloop()


# import tkinter as tk

# cal=tk.Tk()
# cal.geometry=("300*200")

# cal.title("calculator")

# fir=tk.Label(cal,text="first number")
# fir.pack()

# fire=tk.Entry(cal)
# fire.pack()

# sec=tk.Label(cal,text="second number")
# sec.pack()

# secc=tk.Entry(cal)
# secc.pack()

# def say():
#     try:
#         num1 = float(fire.get())
#         num2 = float(secc.get())
#         result = num1 + num2
#         print(f"The addition is {result}")
#     except ValueError:
#         print("Please enter valid numbers")

# button=tk.Button(cal,text="click me",command=say)
# button.pack()

# cal.mainloop()



# import tkinter as tk

# root = tk.Tk()
# root.title("Simple Calculator")


# display = tk.Entry(root, width=50)
# display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# for i in range(4):
#     for j in range(4):
#         btn = tk.Button(root, text="", width=5, height=2)
#         btn.grid(row=i+1, column=j, padx=5, pady=5)


# root.mainloop()


import tkinter as tk

def on_click(char):
    if char == "C":
        entry.delete(0, tk.END)
    elif char == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, char)


root = tk.Tk()
root.title("Calculator")


entry = tk.Entry(root, width=20, font=("Arial", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', 'C', '=', '/'
]


row = 1
col = 0
for b in buttons:
    tk.Button(root, text=b, width=5, height=2, font=("Arial", 14),
              command=lambda ch=b: on_click(ch)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col == 4:
        col = 0
        row += 1


root.mainloop()


