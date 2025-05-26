# import sqlite3

# mybd = sqlite3.connect("data base/collagge.sqlite3")  # Ensure the folder exists

# cursor = mybd.cursor()

# def create_table():
#     sql = """
#         CREATE TABLE IF NOT EXISTS student (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT NOT NULL,
#             email TEXT NOT NULL UNIQUE,
#             address TEXT
#         )
#     """
#     cursor.execute(sql)
#     mybd.commit()

# create_table()

# def select():
#     sql=""" SELECT * FROM students """
#     data = cursor.execute(sql)
#     # print(data.fetchall())
#     # print(data.fetchmany(3))
#     print(data.fetchone())
# select()
# def insert(name, email, address):
#     sql = """
#         INSERT INTO student (name, email, address)
#         VALUES (?, ?, ?)
#     """
#     try:
#         cursor.execute(sql, (name, email, address))
#         mybd.commit()
#         print("Data inserted successfully")
#     except sqlite3.IntegrityError as e:
#         print("Error inserting data:", e)

# # User input
# name = input("Enter your name: ")
# email = input("Enter your email: ")
# address = input("Enter your address: ")

# insert(name, email, address)

# cursor.close()
# mybd.close()

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

conn = sqlite3.connect("data base/product.sqlite3") 
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

def insert(user, news, product):
    sql = """
        INSERT INTO product (user, news, product)
        VALUES (?, ?, ?)
    """
    try:
        cursor.execute(sql, (user, news, product))
        conn.commit()
        print("Data inserted successfully")
    except sqlite3.IntegrityError as e:
        print("Error inserting data:", e)

user = input("Enter your user name: ")
news = input("Enter news: ")
product = input("Enter the product name: ")

insert(user, news, product)

cursor.close()
conn.close()


