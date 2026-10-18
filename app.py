import os
import sqlite3
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# For persistent hosting, set DATABASE_PATH to a persistent disk path.
DB_NAME = os.environ.get("DATABASE_PATH", "data.db")


def init_db():
    parent = os.path.dirname(DB_NAME)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL
            )
        """)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/data", methods=["POST"])
def save_data():
    body = request.get_json(silent=True)
    if not isinstance(body, dict):
        return jsonify({"error": "Dữ liệu không hợp lệ"}), 400

    content = body.get("content")
    if not isinstance(content, str) or not content.strip():
        return jsonify({"error": "Vui lòng nhập nội dung"}), 400
    if len(content) > 1000:
        return jsonify({"error": "Nội dung tối đa 1000 ký tự"}), 400

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.execute(
            "INSERT INTO entries (content) VALUES (?)",
            (content.strip(),)
        )
        new_id = cursor.lastrowid

    return jsonify({"message": "Đã lưu thành công", "id": new_id}), 201


@app.route("/api/data", methods=["GET"])
def get_data():
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT id, content FROM entries ORDER BY id DESC"
        ).fetchall()
    return jsonify([dict(row) for row in rows])


init_db()
