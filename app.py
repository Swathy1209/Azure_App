from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("database.db")

# Create table
conn = get_db()
conn.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    age INTEGER
)
""")
conn.close()

@app.route("/")
def index():
    conn = get_db()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return render_template("index.html", users=users)

@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    email = request.form["email"]
    age = request.form["age"]

    conn = get_db()
    conn.execute("INSERT INTO users(name,email,age) VALUES (?,?,?)",
                 (name,email,age))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM users WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    name = request.form["name"]
    email = request.form["email"]
    age = request.form["age"]

    conn = get_db()
    conn.execute("UPDATE users SET name=?, email=?, age=? WHERE id=?",
                 (name,email,age,id))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run()
