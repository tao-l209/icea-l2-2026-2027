from flask import Flask, render_template_string, request, redirect, url_for, jsonify
from DB.connect import get_db

app = Flask(__name__)

# --- La SOURCE de la page web (HTML) avec Bootstrap ---
PAGE = """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Gestion des Employees</title>
  <!-- Bootstrap 5 CSS -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- Bootstrap Icons -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.css">
  <style>
    body {
      padding: 20px;
      background-color: #f8f9fa;
    }
    .form-container {
      background: white;
      padding: 25px;
      border-radius: 10px;
      box-shadow: 0 0 20px rgba(0,0,0,0.1);
      margin-bottom: 25px;
    }
    .table-container {
      background: white;
      padding: 25px;
      border-radius: 10px;
      box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }
    h1 {
      color: #343a40;
      margin-bottom: 25px;
    }
    h2 {
      color: #495057;
      margin-bottom: 20px;
      padding-bottom: 10px;
      border-bottom: 2px solid #dee2e6;
    }
    .search-container {
      margin-bottom: 20px;
    }
    #searchInput {
      padding: 12px 20px;
      border-radius: 8px;
      border: 2px solid #dee2e6;
      transition: border-color 0.3s;
    }
    #searchInput:focus {
      border-color: #80bdff;
      outline: none;
      box-shadow: 0 0 0 0.25rem rgba(0,123,255,0.25);
    }
    table {
      margin-top: 20px;
    }
    th {
      background-color: #343a40;
      color: white;
      border: none;
    }
    td {
      border-top: 1px solid #dee2e6;
    }
    tr:hover td {
      background-color: #f8f9fa;
    }
    .btn-custom {
      padding: 8px 16px;
      font-size: 14px;
    }
    .action-btn {
      margin-right: 5px;
    }
  </style>
</head>
<body>
  <div class="container-fluid">
    <h1 class="text-center">Gestion des Employees (MySQL / XAMPP)</h1>

    <!-- Formulaire d'ajout -->
    <div class="form-container">
      <h2><i class="bi bi-person-plus me-2"></i> Ajouter un Employee</h2>
      <form id="addForm" method="POST" action="/employees">
        <div class="row g-3">
          <div class="col-md-6">
            <label for="nom" class="form-label fw-bold">Nom</label>
            <input type="text" class="form-control" id="nom" name="nom" required placeholder="Entrez le nom">
          </div>
          <div class="col-md-6">
            <label for="prenom" class="form-label fw-bold">Prenom</label>
            <input type="text" class="form-control" id="prenom" name="prenom" required placeholder="Entrez le prenom">
          </div>
        </div>
        <div class="d-flex justify-content-end gap-2 mt-4">
          <button type="reset" class="btn btn-secondary btn-custom">
            <i class="bi bi-x-circle me-1"></i> Annuler
          </button>
          <button type="submit" class="btn btn-primary btn-custom">
            <i class="bi bi-check-circle me-1"></i> Ajouter
          </button>
        </div>
      </form>
    </div>

    <!-- Barre de recherche et liste -->
    <div class="table-container">
      <!-- Messages -->
      {% if message %}
      <div class="alert alert-success alert-dismissible fade show" role="alert">
        {{ message }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
      {% endif %}
      {% if error %}
      <div class="alert alert-danger alert-dismissible fade show" role="alert">
        {{ error }}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
      </div>
      {% endif %}

      <div class="search-container">
        <input type="text" id="searchInput" class="form-control" onkeyup="filtrerTableau()" 
               placeholder="Rechercher par ID, nom ou prenom...">
      </div>

      <div class="table-responsive">
        <table id="userTable" class="table table-hover">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nom</th>
              <th>Prenom</th>
              <th class="text-center">Actions</th>
            </tr>
          </thead>
          <tbody>
            {% for u in employees %}
            <tr>
              <td>{{ u[0] }}</td>
              <td>{{ u[1] }}</td>
              <td>{{ u[2] }}</td>
              <td class="text-center">
                <button class="btn btn-sm btn-outline-success action-btn" 
                        onclick="editEmployee({{ u[0] }}, '{{ u[1] }}', '{{ u[2] }}')">
                  <i class="bi bi-pencil"></i> Modifier
                </button>
                <button class="btn btn-sm btn-outline-danger action-btn" 
                        onclick="deleteEmployee({{ u[0] }})">
                  <i class="bi bi-trash"></i> Supprimer
                </button>
              </td>
            </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
    </div>

    <!-- Modal de modification -->
    <div id="editModal" class="modal" tabindex="-1">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title"><i class="bi bi-pencil-square me-2"></i> Modifier Employee</h5>
            <button type="button" class="btn-close" onclick="closeModal()" aria-label="Close"></button>
          </div>
          <form id="editForm" method="POST" action="">
            <div class="modal-body">
              <input type="hidden" id="editId" name="id">
              <div class="mb-3">
                <label for="editNom" class="form-label fw-bold">Nom</label>
                <input type="text" class="form-control" id="editNom" name="nom" required>
              </div>
              <div class="mb-3">
                <label for="editPrenom" class="form-label fw-bold">Prenom</label>
                <input type="text" class="form-control" id="editPrenom" name="prenom" required>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" onclick="closeModal()">
                <i class="bi bi-x-circle me-1"></i> Annuler
              </button>
              <button type="submit" class="btn btn-primary">
                <i class="bi bi-check-circle me-1"></i> Enregistrer
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>

  <!-- Bootstrap 5 JS Bundle with Popper -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>

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

    function editEmployee(id, nom, prenom) {
      document.getElementById("editId").value = id;
      document.getElementById("editNom").value = nom;
      document.getElementById("editPrenom").value = prenom;
      document.getElementById("editForm").action = "/employees/" + id;
      const modal = new bootstrap.Modal(document.getElementById("editModal"));
      modal.show();
    }

    function deleteEmployee(id) {
      if (confirm("Etes-vous sur de vouloir supprimer cet employee?")) {
        fetch("/employees/" + id, {
          method: "DELETE"
        }).then(response => {
          if (response.ok) {
            window.location.reload();
          } else {
            alert("Erreur lors de la suppression");
          }
        });
      }
    }

    function closeModal() {
      const modal = bootstrap.Modal.getInstance(document.getElementById("editModal"));
      if (modal) modal.hide();
    }
  </script>
</body>
</html>
"""


@app.route('/')
def index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id, nom, prenom FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template_string(PAGE, employees=employees, message=request.args.get('message'), error=request.args.get('error'))


@app.route('/employees', methods=['POST'])
def create_employee():
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    
    if not nom or not prenom:
        return redirect(url_for('index', error='Nom et Prenom sont requis'))
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO employees (nom, prenom) VALUES (%s, %s)", (nom, prenom))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for('index', message='Employee ajoute avec succes'))
    except Exception as e:
        return redirect(url_for('index', error=f'Erreur: {str(e)}'))


@app.route('/employees/<int:employee_id>', methods=['POST'])
def update_employee(employee_id):
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')
    
    if not nom or not prenom:
        return redirect(url_for('index', error='Nom et Prenom sont requis'))
    
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("UPDATE employees SET nom=%s, prenom=%s WHERE id=%s", (nom, prenom, employee_id))
        db.commit()
        cursor.close()
        db.close()
        return redirect(url_for('index', message='Employee mis a jour avec succes'))
    except Exception as e:
        return redirect(url_for('index', error=f'Erreur: {str(e)}'))


@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM employees WHERE id=%s", (employee_id,))
        db.commit()
        cursor.close()
        db.close()
        return jsonify({'success': True, 'message': 'Employee supprime avec succes'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
