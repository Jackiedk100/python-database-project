import sqlite3
conn = sqlite3.connect('books.db')
cursor = conn.cursor()


cursor.execute("""SELECT books.title, authors.name, books.release_date
FROM books
JOIN authors ON books.author_id = authors.id
""")

results = cursor.fetchall()
for row in results:
    print(row)

conn.commit()
conn.close()
