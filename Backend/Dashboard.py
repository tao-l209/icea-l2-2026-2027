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
    # 1. Indicateurs clés (KPI)
    kpis = {
        "revenus": "42 500 €",
        "utilisateurs": 1280,
        "croissance": "+14 %"
    }
    
    # 2. Données pour le graphique
    mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin"]
    ventes = [1000, 1500, 2000, 1800, 2500, 3000]
    
    employees = get_employees()
    
    return render_template(
        "dashboard.html",
        kpis=kpis,
        mois=mois,
        ventes=ventes,
        employees=employees,
    )

if __name__ == "__main__":
    app.run(debug=True)
