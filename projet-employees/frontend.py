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
    body { font-family: Arial, sans-serif; margin: 40px; background: #f4f4f4; }
    h1 { color: #333; }

    /* Style de la barre de recherche */
    .search-container {
      margin-bottom: 20px;
      width: 60%;
    }
    #searchInput {
      width: 100%;
      padding: 12px 15px;
      font-size: 16px;
      border: 1px solid #ccc;
      border-radius: 5px;
      box-sizing: border-box; /* Garde la largeur alignée avec le tableau */
      outline: none;
      transition: border-color 0.3s;
    }
    #searchInput:focus {
      border-color: #2c7be5;
    }

    /* Style du tableau */
    table { border-collapse: collapse; width: 60%; background: white; }
    th, td { border: 1px solid #ccc; padding: 10px; text-align: left; }
    th { background: #2c7be5; color: white; }
    tr:hover { background-color: #f9f9f9; }
  </style>
</head>
<body>
  <h1>Utilisateurs (depuis MySQL / XAMPP)</h1>

  <!-- Barre de recherche -->
  <div class="search-container">
    <input type="text" id="searchInput" onkeyup="filtrerTableau()" placeholder="Rechercher par ID, nom ou email...">
  </div>

  <table id="userTable">
    <thead>
      <tr>
        <th>ID</th>
        <th>Nom</th>
        <th>Email</th>
      </tr>
    </thead>
    <tbody>
      {% for u in employees %}
      <tr>
        <td>{{ u[0] }}</td>
        <td>{{ u[1] }}</td>
        <td>{{ u[2] }}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>

  <!-- Script pour rendre la recherche fonctionnelle en direct -->
  <script>
    function filtrerTableau() {
      const input = document.getElementById("searchInput");
      const filter = input.value.toLowerCase();
      const table = document.getElementById("userTable");
      const tr = table.getElementsByTagName("tr");

      // Parcourt toutes les lignes (en ignorant l'en-tête à l'index 0)
      for (let i = 1; i < tr.length; i++) {
        const rowText = tr[i].textContent.toLowerCase();
        tr[i].style.display = rowText.includes(filter) ? "" : "none";
      }
    }
  </script>
</body>
</html>

"""

@app.route("/")
def index():
    employees = get_employees()
    return render_template_string(PAGE, employees=employees)
