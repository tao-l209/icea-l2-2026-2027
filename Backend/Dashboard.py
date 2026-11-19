from pathlib import Path

from flask import Flask, render_template

import mysql.connector

app = Flask(__name__, template_folder=str(Path(__file__).resolve().parent))


def get_employees():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db_employees2",
    )
    try:
        with db.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT id, nom, prenom FROM employees ORDER BY id")
            return cursor.fetchall()
    finally:
        db.close()


@app.route("/")
@app.route("/dashboard")
@app.route("/dashboard.html")
def index():
    employees = get_employees()
    return render_template("dashboard.html", employees=employees)

if __name__ == "__main__":
    app.run(debug=True)
