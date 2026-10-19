import sqlite3
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

author = input(f'Please enter the authors name you wish to add to the database')
cursor.execute("INSERT INTO authors (name) VALUES ('')")
cursor.execute("SELECT * FROM authors")


