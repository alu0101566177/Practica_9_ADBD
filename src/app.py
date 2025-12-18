import os
import psycopg2
from flask import Flask, render_template, request, url_for, redirect
import logging

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
        database="flask_db",
		user="user",
        password="user")
    return conn


@app.route('/')
def index():
    conn = None
    try:
        # 1. Intentar establecer conexión
        conn = get_db_connection()
        cur = conn.cursor()
        
        # 2. Ejecutar la consulta
        cur.execute('SELECT * FROM books;')
        books = cur.fetchall()
        
        # 3. Limpiar cursor
        cur.close()
        return render_template('index.html', books=books)

    except Exception as e:
        # Registrar el error real en la consola/log para el desarrollador
        logging.error(f"Error al acceder a la base de datos: {e}")
        
        # Opcional: Enviar un mensaje de error a la interfaz (requiere flash en Flask)
        # flash("No se pudieron cargar los libros en este momento.")
        
        return render_template('index.html', books=[], error="Error de conexión")

    finally:
        # 4. Asegurar que la conexión se cierre SIEMPRE, haya error o no
        if conn is not None:
            conn.close()

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages_num = int(request.form['pages_num'])
        review = request.form['review']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s)',
                    (title, author, pages_num, review))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')