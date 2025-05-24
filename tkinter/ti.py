import tkinter as tk
from tkinter import ttk

window =tk .Tk()

window.title("info")   

window.minsize(400,400)    
window.maxsize(1000,1000) 

tx=ttk.Label(window,text="information")
tx.grid(column=0, row=0, columnspan=2, pady=10)

name = ttk.Label(window, text='enter your Name:')
name.grid(column=0, row=1, padx=10, pady=10)


entry = ttk.Entry(window)
entry.grid(column=1,row=1,padx=10,pady=10)
entry.focus()


label = ttk.Label(window, text='enter your address:')
label.grid(column=0,row=2,padx=10,pady=10)

entry = ttk.Entry(window)
entry.grid(column=1,row=2,padx=5,pady=5)
entry.focus()

def button_clicked():
    name_value=name.get()
    print(f"hello {name_value}")


button = ttk.Button(window, text='exit', command=button_clicked)
button.grid(column=1,row=3)

window.config(background='white')  

window.mainloop()
