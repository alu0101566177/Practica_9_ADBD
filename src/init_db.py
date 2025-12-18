import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
		user='user',
        password='user')

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'pages_num integer NOT NULL,'
                                 'review text,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('A Tale of Two Cities',
             'Charles Dickens',
             489,
             'A great classic!')
            )


cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy',
             864,
             'Another great classic!')
            )

# 1. 1984
cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('1984',
             'George Orwell',
             328,
             'Una distopía inquietante y visionaria.')
            )

# 2. El Gran Gatsby
cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('The Great Gatsby',
             'F. Scott Fitzgerald',
             180,
             'Un retrato fascinante de la era del jazz.')
            )

# 3. Cien años de soledad
cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('One Hundred Years of Solitude',
             'Gabriel García Márquez',
             417,
             'La obra maestra del realismo mágico.')
            )

# 4. Orgullo y Prejuicio
cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Pride and Prejudice',
             'Jane Austen',
             279,
             'Un romance clásico e inteligente.')
            )

# 5. El Hobbit
cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('The Hobbit',
             'J.R.R. Tolkien',
             310,
             'Una aventura épica e inolvidable.')
            )

# 6. Un Mundo Feliz
cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Brave New World',
             'Aldous Huxley',
             268,
             'Una crítica social profunda y actual.')
            )

# 7. El Guardián entre el Centeno
cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('The Catcher in the Rye',
             'J.D. Salinger',
             234,
             'La esencia de la angustia adolescente.')
            )

# 8. Matar a un Ruiseñor
cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('To Kill a Mockingbird',
             'Harper Lee',
             281,
             'Un relato poderoso sobre la justicia y la moral.')
            )

# 9. Moby Dick
cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Moby Dick',
             'Herman Melville',
             635,
             'Una obsesión profunda en alta mar.')
            )

# 10. El Alquimista
cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('The Alchemist',
             'Paulo Coelho',
             208,
             'Una fábula inspiradora sobre seguir tus sueños.')
            )

conn.commit()

cur.close()
conn.close()