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

# conn = sqlite3.connect("data base/product.sqlite3") 
# cursor = conn.cursor()

# def create_product():
#     sql = """
#         CREATE TABLE IF NOT EXISTS product (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             user TEXT NOT NULL,
#             news TEXT NOT NULL UNIQUE,
#             product TEXT
#         )
#     """
#     cursor.execute(sql)
#     conn.commit()

# create_product()

# def insert(user, news, product):
#     sql = """
#         INSERT INTO product (user, news, product)
#         VALUES (?, ?, ?)
#     """
#     try:
#         cursor.execute(sql, (user, news, product))
#         conn.commit()
#         print("Data inserted successfully")
#     except sqlite3.IntegrityError as e:
#         print("Error inserting data:", e)

# # User input
# user = input("Enter your user name: ")
# news = input("Enter news: ")
# product = input("Enter the product name: ")

# insert(user, news, product)

# cursor.close()
# conn.close()


