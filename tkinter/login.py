import tkinter as tk

window =tk .Tk()

def check_login():
    user = uname.get()
    pwd = pas.get()
    if user == 'admin' and pwd == 'admin123':
        result_label.config(text="The password is correct", fg="green")
        root=tk .Tk()
        lab=tk.Label(root,text="login ")
        lab.grid(column=0, row=0, padx=10, pady=10)
        root.title("login")

        root.mainloop
    else:
        result_label.config(text="The password is incorrect", fg="red")
        
window.minsize(400,400)    
window.maxsize(1000,1000)
window.title("log in")
username=tk.Label(window,text="username")
username.grid(column=0, row=0, padx=10, pady=10)

uname=tk.Entry(window)
uname.grid(column=1, row=0, padx=10, pady=10)


password=tk.Label(window,text="password")
password.grid(column=0,row=2,padx=10,pady=10)

pas=tk.Entry(window)
pas.grid(column=1,row=2,padx=10,pady=10)

result_label = tk.Label(window, text="")
result_label.grid(column=1, row=3, pady=10)

button = tk.Button(window, text="Login", command=check_login)
button.grid(column=1, row=4, pady=10)


window.mainloop()

