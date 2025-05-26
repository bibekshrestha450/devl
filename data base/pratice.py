# import sqlite3

# conn = sqlite3.connect("database/college.sqlite3")
# mycur =conn.cursor()
# def create_table():
#     sql="""
#         CREATE TABLE IF NOT EXISTS students (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT NOT NULL UNIQUE,
#             address TEXT
#         )
#     """
#     mycur.execute(sql)
# create_table()

# def select():
#     sql=""" SELECT * FROM students """
#     data = mycur.execute(sql)
#     print(data.fetchall())


# def insert(name,email,address):
#     sql="""
#         INSERT INTO students (name, email, address)
#         VALUES (?, ?, ?)
#         """
#     mycur.execute(sql, (name, email, address))
#     conn.commit()
#     print("Data inserted successfully.")


# def update(name,email,address,id):
#     sql="""
#         UPDATE students SET name = ?, email = ?, address = ? WHERE id = ?
#         """
#     mycur.execute(sql, (name, email, address, id))
#     conn.commit()
#     print("Data Update successfully.")


# def delete(id):
#     sql="""
#         DELETE FROM students WHERE id = ?
#         """
#     mycur.execute(sql, (id,))
#     conn.commit()
#     print("Data Deleted successfully.")



# print("1. Insert Data 2. View Data 3. Update Data 4. Delete Data")
# option=int(input("Enter option: "))
# if option ==1:   
#     name = input("Enter name: ")
#     email = input("Enter email: ")
#     address = input("Enter address: ")
#     insert(name, email, address)
# elif option == 2:
#     select()
# elif option == 3:
#     name = input("Enter name: ")
#     email = input("Enter email: ")
#     address = input("Enter address: ")
#     id = input("Enter id: ")
#     update(name, email, address, id)
# elif option == 4:
#     id = input("Enter id: ")
#     delete(id)
# else:
#     print("Invalid option selected.")


import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect("product.sqlite3")
cursor = conn.cursor()

def create_product():
    sql = """
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT NOT NULL,
            news TEXT NOT NULL UNIQUE,
            product TEXT
        )
    """
    cursor.execute(sql)
    conn.commit()

create_product()

def insert(user,news,product):
    sql="""
        INSERT INTO students (user, news, product)
        VALUES (?, ?, ?)
        """
    cursor.execute(sql, (user,news,product))
    conn.commit()
    print("Data inserted successfully.")


def select():
    sql=""" SELECT * FROM product """
    data = cursor.execute(sql)
    print(data.fetchall())

def update_data():
    id_val = int(id_entry.get())
    user = user_entry.get()
    news = news_entry.get()
    product = product_entry.get()

    cursor.execute("UPDATE product SET user = ?, news = ?, product = ? WHERE id = ?", (user, news, product, id_val))
    conn.commit()
    messagebox.showinfo("Success", "Data updated successfully.")
    select()

def delete(id):
        sql="""
            DELETE FROM students WHERE id = ?
            """
        cursor.execute(sql, (id,))
        conn.commit()
        print("Data Deleted successfully.")

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

tk.Label(root, text="ID for Update/Delete:").pack()
id_entry = tk.Entry(root, width=40)
id_entry.pack()


tk.Button(root, text="Insert", command=insert).pack(pady=10)

tk.Button(root,text="view data", command=select).pack(pady=10)

tk.Button(root,text="update data", command=update_data).pack(pady=10)

tk.Button(root,text="delet data", command=delete).pack(pady=10)
status_label = tk.Label(root, text="", fg="blue")
status_label.pack()

tk.Label(root, text="Stored Data:").pack()
listbox = tk.Listbox(root, width=70, height=10)
listbox.pack()

root.mainloop()
cursor.close()
conn.close()


# import sqlite3
# import tkinter as tk
# from tkinter import messagebox

# # Connect to the database
# conn = sqlite3.connect("product.sqlite3")
# cursor = conn.cursor()

# # Create the table if it doesn't exist
# def create_product():
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS product (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user TEXT NOT NULL,
#             news TEXT NOT NULL UNIQUE,
#             product TEXT
#         )
#     """)
#     conn.commit()

# create_product()

# # Insert data into the table
# def insert_data():
#     user = user_entry.get()
#     news = news_entry.get()
#     product = product_entry.get()

#     cursor.execute("INSERT INTO product (user, news, product) VALUES (?, ?, ?)", (user, news, product))
#     conn.commit()
#     messagebox.showinfo("Success", "Data inserted successfully.")
#     select_data()

# # View all data
# def select_data():
#     listbox.delete(0, tk.END)
#     cursor.execute("SELECT * FROM product")
#     rows = cursor.fetchall()
#     for row in rows:
#         listbox.insert(tk.END, row)

# # Update data by ID
# def update_data():
#     id_val = int(id_entry.get())
#     user = user_entry.get()
#     news = news_entry.get()
#     product = product_entry.get()

#     cursor.execute("UPDATE product SET user = ?, news = ?, product = ? WHERE id = ?", (user, news, product, id_val))
#     conn.commit()
#     messagebox.showinfo("Success", "Data updated successfully.")
#     select_data()

# # Delete data by ID
# def delete_data():
#     id_val = int(id_entry.get())

#     cursor.execute("DELETE FROM product WHERE id = ?", (id_val,))
#     conn.commit()
#     messagebox.showinfo("Success", "Data deleted successfully.")
#     select_data()

# root = tk.Tk()
# root.title("Product Entry")
# root.geometry("500x500")

# tk.Label(root, text="User:").pack()
# user_entry = tk.Entry(root, width=40)
# user_entry.pack()

# tk.Label(root, text="News:").pack()
# news_entry = tk.Entry(root, width=40)
# news_entry.pack()

# tk.Label(root, text="Product:").pack()
# product_entry = tk.Entry(root, width=40)
# product_entry.pack()

# tk.Label(root, text="ID (for Update/Delete):").pack()
# id_entry = tk.Entry(root, width=40)
# id_entry.pack()

# tk.Button(root, text="Insert", command=insert_data).pack(pady=5)
# tk.Button(root, text="View Data", command=select_data).pack(pady=5)
# tk.Button(root, text="Update Data", command=update_data).pack(pady=5)
# tk.Button(root, text="Delete Data", command=delete_data).pack(pady=5)

# tk.Label(root, text="Stored Data:").pack()
# listbox = tk.Listbox(root, width=70, height=10)
# listbox.pack()

# root.mainloop()

# cursor.close()
# conn.close()
