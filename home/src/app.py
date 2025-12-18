from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Configuración de conexión (ajusta con tus credenciales)
def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="myhome",
        user="user",
        password="user"
    )

# 1. Temperatura media de todas las habitaciones
@app.route('/api/temperatures/average', methods=['GET'])
def get_global_average():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT AVG(temperature) FROM temperatures;')
        avg_temp = cur.fetchone()[0]
        return jsonify({'average_temperature': avg_temp})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn: conn.close()

# 2. Temperatura máxima en las habitaciones
@app.route('/api/temperatures/max', methods=['GET'])
def get_global_max():
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT MAX(temperature) FROM temperatures;')
        max_temp = cur.fetchone()[0]
        return jsonify({'max_temperature': max_temp})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn: conn.close()

# 3. Nombre de la habitación dado el room_id
@app.route('/api/rooms/<int:room_id>/name', methods=['GET'])
def get_room_name(room_id):
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT name FROM rooms WHERE id = %s;', (room_id,))
        result = cur.fetchone()
        if result:
            return jsonify({'room_id': room_id, 'name': result[0]})
        return jsonify({'message': 'Room not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn: conn.close()

# 4. Temperatura media histórica de una habitación específica
@app.route('/api/rooms/<int:room_id>/average', methods=['GET'])
def get_room_average(room_id):
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT AVG(temperature) FROM temperatures WHERE room_id = %s;', (room_id,))
        avg_temp = cur.fetchone()[0]
        return jsonify({'room_id': room_id, 'average_temperature': avg_temp})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn: conn.close()

# 5. Temperatura mínima y nombre de la habitación (JSON)
@app.route('/api/rooms/<int:room_id>/min-stats', methods=['GET'])
def get_room_min_stats(room_id):
    conn = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # Usamos un JOIN para obtener datos de ambas tablas en una sola consulta
        query = """
            SELECT r.name, MIN(t.temperature) 
            FROM rooms r 
            LEFT JOIN temperatures t ON r.id = t.room_id 
            WHERE r.id = %s 
            GROUP BY r.name;
        """
        cur.execute(query, (room_id,))
        result = cur.fetchone()
        
        if result:
            return jsonify({
                'room_id': room_id,
                'name': result[0],
                'min_temperature': result[1]
            })
        return jsonify({'message': 'Room not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if conn: conn.close()

if __name__ == '__main__':
    app.run(debug=True)