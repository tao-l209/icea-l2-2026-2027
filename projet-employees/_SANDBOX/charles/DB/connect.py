import mysql.connector

# --- Connexion a MySQL de XAMPP ---
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",          # utilisateur par defaut de XAMPP
        password="",          # mot de passe vide par defaut
        database="db_employees2"
    )

def get_employees():
    db = get_db()
    curseur = db.cursor()
    curseur.execute("SELECT id, nom, prenom FROM employees")
    employees = curseur.fetchall()
    curseur.close()
    db.close()
    return employees
