from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask import redirect
from flask import url_for
from flask import session

import sqlite3

app = Flask(__name__)
app.secret_key = "finalyearproject"

# --------------------
# Database
# --------------------

def init_db():

    conn = sqlite3.connect("database.db")

    cur = conn.cursor()

    cur.execute("""

    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username TEXT,

        password TEXT

    )

    """)

    conn.commit()
    conn.close()

init_db()

# --------------------
# AI Response
# --------------------

def generate_ai_response(query):

    return f"""

Topic:
{query}

Summary:
{query} is a rapidly growing research area.

Applications:

• Healthcare

• Education

• Artificial Intelligence

• Manufacturing

Patent Opportunities:

• Smart Analytics Systems

• AI Prediction Engines

• Automated Research Platforms

Future Scope:

Strong growth expected.

"""

# --------------------
# Routes
# --------------------

@app.route("/")
def home():

    if "user" not in session:
        return redirect("/login")

    return render_template("index.html")

@app.route("/login")
def login():

    return render_template("login.html")

@app.route("/register")
def register():

    return render_template("register.html")

@app.route("/register_user", methods=["POST"])
def register_user():

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users(username,password) VALUES(?,?)",
        (username,password)
    )

    conn.commit()
    conn.close()

    return redirect("/login")

@app.route("/login_user", methods=["POST"])
def login_user():

    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username,password)
    )

    user = cur.fetchone()

    conn.close()

    if user:

        session["user"] = username

        return redirect("/")

    return redirect("/login")

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")

@app.route("/search", methods=["POST"])
def search():

    data = request.json

    query = data.get("query")

    result = generate_ai_response(query)

    return jsonify({

        "result": result

    })

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )