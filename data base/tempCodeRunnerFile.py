import sqlite3
import tkinter as tk


conn = sqlite3.connect("product.sqlite3")
cursor = conn.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT NOT NULL,
            news TEXT NOT NULL UNIQUE,
            product TEXT
        )
    """)
    conn.commit()

create_table()

def insert_data():
    user = user_entry.get()
    news = news_entry.get()
    product = product_entry.get()

    if user != "" and news != "":
        cursor.execute("INSERT INTO product (user, news, product) VALUES (?, ?, ?)",
                       (user, news, product))
        conn.commit()
        status_label.config(text="Data inserted.")
        show_data()
    else:
        status_label.config(text="User and News are required.")

def show_data():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()
    for row in rows:
        listbox.insert(tk.END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")

root = tk.Tk()
root.title("Product Entry")
root.geometry("500x400")


tk.Label(root, text="User:").pack()
user_entry = tk.Entry(root, width=40)
user_entry.pack()

tk.Label(root, text="News:").pack()
news_entry = tk.Entry(root, width=40)
news_entry.pack()

tk.Label(root, text="Product:").pack()
product_entry = tk.Entry(root, width=40)
product_entry.pack()

tk.Button(root, text="Insert", command=insert_data).pack(pady=10)

status_label = tk.Label(root, text="", fg="blue")
status_label.pack()

tk.Label(root, text="Stored Data:").pack()
listbox = tk.Listbox(root, width=70, height=10)
listbox.pack()

show_data()
root.mainloop()
cursor.close()
conn.close()