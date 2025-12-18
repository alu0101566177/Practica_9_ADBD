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
        # 1. Obtención de datos con limpieza básica
        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        pages_num_raw = request.form.get('pages_num', '')
        review = request.form.get('review', '').strip()

        # 2. Validación y manejo de NULOS
        # Convertimos strings vacíos a None para que la DB los trate como NULL
        title = title if title else None
        author = author if author else None
        review = review if review else None
        
        # Validación especial para el entero (evita error al convertir string vacío)
        try:
            pages_num = int(pages_num_raw) if pages_num_raw else None
        except ValueError:
            # Aquí podrías retornar un error al usuario indicando que el número no es válido
            return "El número de páginas debe ser un valor numérico", 400

        conn = None
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            
            # 3. Inserción segura
            cur.execute('INSERT INTO books (title, author, pages_num, review)'
                        'VALUES (%s, %s, %s, %s)',
                        (title, author, pages_num, review))
            
            # 4. Confirmar los cambios
            conn.commit()
            cur.close()
            return redirect(url_for('index'))

        except Exception as e:
            # 5. Deshacer cambios en caso de error (Rollback)
            if conn:
                conn.rollback()
            logging.error(f"Error al insertar registro: {e}")
            return "Ocurrió un error al guardar el libro.", 500

        finally:
            # 6. Cierre seguro de la conexión
            if conn:
                conn.close()

    return render_template('create.html')