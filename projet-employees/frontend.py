from flask import Flask, render_template_string
from DB.connect import get_employees

app = Flask(__name__)

# --- La SOURCE de la page web (HTML) ---
PAGE = """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Liste des utilisateurs</title>
  <style>
    body { font-family: Arial; margin: 40px; background: #f4f4f4; }
    table { border-collapse: collapse; width: 60%; background: white; }
    th, td { border: 1px solid #ccc; padding: 10px; text-align: left; }
    th { background: #2c7be5; color: white; }
    h1 { color: #333; }
  </style>
</head>
<body>
  <h1>Utilisateurs (depuis MySQL / XAMPP)</h1>
  <table>
    <tr><th>ID</th><th>Nom</th><th>Email</th></tr>
    {% for u in employees %}
    <tr>
      <td>{{ u[0] }}</td>
      <td>{{ u[1] }}</td>
      <td>{{ u[2] }}</td>
    </tr>
    {% endfor %}
  </table>
</body>
</html>
"""

@app.route("/")
def index():
    employees = get_employees()
    return render_template_string(PAGE, employees=employees)
