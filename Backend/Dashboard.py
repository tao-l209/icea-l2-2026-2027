from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__, template_folder=str(Path(__file__).resolve().parent))

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
    
    # 3. Données pour un tableau récapitulatif
    Employees = [
        {"id": "1", "Noms": "...", "Prénoms": "..."},
        {"id": "2", "Noms": "...", "Prénoms": "..."},
        {"id": "3", "Noms": "...", "Prénoms": "..."},
    ]
    
    return render_template(
        "dashboard.html", 
        kpis=kpis,
        mois=mois, 
        ventes=ventes, 
        Employees=Employees
    )

if __name__ == "__main__":
    app.run(debug=True)
