import sqlite3

# Connect to the database
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Characters allowed in an author name besides letters
allowed_extra_chars = " .-'"
max_name_length = 100

# Keep asking for authors until the user types q
while True:
    author = input("Please enter the author name you wish to add to the database (or q to quit): ").strip()

    # Stop the program if the user types q
    if author.lower() == "q":
        break

    # Check that the name is not empty (strip() also removes whitespace-only input)
    if author == "":
        print("Author name cannot be empty or just whitespace. Please try again.")
        continue

    # Check the length
    if len(author) > max_name_length:
        print(f"Author name cannot be longer than {max_name_length} characters. Please try again.")
        continue

    # Check that the name contains no digits
    if any(char.isdigit() for char in author):
        print("Author name cannot contain digits. Please try again.")
        continue

    # Check that the name only contains letters and the allowed special characters
    if not all(char.isalpha() or char in allowed_extra_chars for char in author):
        print("Author name can only contain letters, spaces, '.', '-' and apostrophes. Please try again.")
        continue

    # Check if the author already exists (case-insensitive)
    cursor.execute("SELECT id FROM authors WHERE LOWER(name) = LOWER(?)", (author,))
    existing_author = cursor.fetchone()

    if existing_author:
        print(f'Author "{author}" already exists in the database with ID: {existing_author[0]}. Please try again.')
        continue

    # All checks passed, so insert the new author
    cursor.execute("INSERT INTO authors (name) VALUES (?)", (author,))
    conn.commit()

    print(f'Author "{author}" has been added to the database.')

    # Fetch the new author from the database and print it
    cursor.execute("SELECT * FROM authors WHERE name = ?", (author,))
    results = cursor.fetchall()

    for author_id, name in results:
        print(f"ID: {author_id}, Author: {name}")

conn.close()