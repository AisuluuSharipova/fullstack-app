from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

def get_db():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            student_name TEXT NOT NULL,
            student_id TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT id, title, student_name, student_id FROM tasks ORDER BY created_at DESC")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify([{
            "id": r[0], "title": r[1],
            "student_name": r[2], "student_id": r[3]
        } for r in rows])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/data', methods=['POST'])
def add_data():
    data = request.get_json()
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO tasks (title, student_name, student_id) VALUES (%s, %s, %s) RETURNING id",
            (data['title'], data['student_name'], data['student_id'])
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"id": new_id, "message": "Добавлено"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/data/<int:item_id>', methods=['DELETE'])
def delete_data(item_id):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM tasks WHERE id = %s", (item_id,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "Удалено"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

def get_db():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            student_name TEXT NOT NULL,
            student_id TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT id, title, student_name, student_id FROM tasks ORDER BY created_at DESC")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify([{
            "id": r[0], "title": r[1],
            "student_name": r[2], "student_id": r[3]
        } for r in rows])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/data', methods=['POST'])
def add_data():
    data = request.get_json()
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO tasks (title, student_name, student_id) VALUES (%s, %s, %s) RETURNING id",
            (data['title'], data['student_name'], data['student_id'])
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"id": new_id, "message": "Добавлено"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/data/<int:item_id>', methods=['DELETE'])
def delete_data(item_id):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM tasks WHERE id = %s", (item_id,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "Удалено"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

def get_db():
    return psycopg2.connect(os.environ.get("DATABASE_URL"))

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            student_name TEXT NOT NULL,
            student_id TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT id, title, student_name, student_id FROM tasks ORDER BY created_at DESC")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify([{
            "id": r[0], "title": r[1],
            "student_name": r[2], "student_id": r[3]
        } for r in rows])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/data', methods=['POST'])
def add_data():
    data = request.get_json()
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO tasks (title, student_name, student_id) VALUES (%s, %s, %s) RETURNING id",
            (data['title'], data['student_name'], data['student_id'])
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"id": new_id, "message": "Добавлено"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/data/<int:item_id>', methods=['DELETE'])
def delete_data(item_id):
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM tasks WHERE id = %s", (item_id,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "Удалено"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    init_db()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
