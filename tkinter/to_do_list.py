import tkinter as tk

def add():
    task = enter.get()
    if task:
        listbox.insert(tk.END, task)


win=tk .Tk()
win.title("to do list")

enter=tk.Entry(win)
enter.pack()

add_button = tk.Button(win, text="Add Task", command=add)
add_button.pack()


listbox = tk.Listbox(win, width=40)
listbox.pack()

win.mainloop()