import sqlite3
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute("""
DELETE FROM books
""")

cursor.execute("""
DELETE FROM authors
""")

conn.commit()
conn.close()



