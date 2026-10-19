import sqlite3
conn = sqlite3.connect('books.db')
cursor = conn.cursor()


cursor.execute("""SELECT books.title, authors.name, books.release_date
FROM books
JOIN authors ON books.author_id = authors.id
""")

results = cursor.fetchall()
for title, author, release_date in results:
    print(f"Titel: {title} \nForfatter: {author} \nUdgivelsesdato: {release_date}\n\n")

conn.commit()
conn.close()
