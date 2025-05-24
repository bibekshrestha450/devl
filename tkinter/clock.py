# import tkinter as tk
# import time

# def update_time():
#     current_time = time.strftime("%H:%M:%S")
#     clock_label.config(text=current_time)
#     clock_label.after(1000, update_time)


# root = tk.Tk()
# root.title("Digital Clock")
# root.geometry("300x150")
# root.configure(bg="black")

# clock_label = tk.Label(root, font=('Arial', 50), fg='cyan', bg='black')
# clock_label.pack(pady=20)

# update_time()

# root.mainloop()


import tkinter as tk
import time

def tim():
    curtime=time.strftime("%H,%M,%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

root=tk .Tk()
root.title("time")
root.geometry("300x150")
root.configure(bg="black")

clock_label = tk.Label(root, font=('Arial', 50), fg='cyan', bg='black')
clock_label.pack(pady=20)

tim()

root.mainloop()