import array
from collections import deque, namedtuple
from itertools import groupby
import json
import os
import sys

from flask import Flask, render_template_string
from flask_bootstrap import Bootstrap5

# Permet d'importer DB.connect même si le script est lancé depuis _SANDBOX/
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from DB.connect import get_db

app = Flask(__name__)
bootstrap = Bootstrap5(app)


def fetch_all_tables():
    """Récupère les données brutes des 3 tables de db_employees2."""
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT id, nom FROM colors ORDER BY id")
    colors_raw = cursor.fetchall()  # liste de tuples: [(1, 'bleu'), ...]

    cursor.execute("SELECT id, type FROM dextre ORDER BY id")
    dextre_raw = cursor.fetchall()  # liste de tuples: [(1, 'droitier'), ...]

    cursor.execute("SELECT id, nom, prenom FROM employees ORDER BY id")
    employees_raw = cursor.fetchall()  # liste de tuples: [(1, 'Dupont', 'Jean'), ...]

    cursor.close()
    db.close()
    return colors_raw, dextre_raw, employees_raw


def build_structures(colors_raw, dextre_raw, employees_raw):
    """Construit différentes structures de données pour les 3 tables."""

    # 1. LISTE (listes standards Python)
    liste_data = {
        "colors": [list(row) for row in colors_raw],
        "dextre": [list(row) for row in dextre_raw],
        "employees": [list(row) for row in employees_raw],
    }

    # 2. TUPLE (tuples imbriqués)
    tuple_data = {
        "colors": tuple(colors_raw),
        "dextre": tuple(dextre_raw),
        "employees": tuple(employees_raw),
    }

    # 3. NAMEDTUPLE (tuple nommé)
    ColorNT = namedtuple("ColorNT", ["id", "nom"])
    DextreNT = namedtuple("DextreNT", ["id", "type"])
    EmployeeNT = namedtuple("EmployeeNT", ["id", "nom", "prenom"])
    namedtuple_data = {
        "colors": [ColorNT(*r) for r in colors_raw],
        "dextre": [DextreNT(*r) for r in dextre_raw],
        "employees": [EmployeeNT(*r) for r in employees_raw],
    }

    # 4. ARRAY (module standard `array` typé sur les IDs entiers 'i')
    array_data = {
        "colors_ids": array.array("i", [r[0] for r in colors_raw]),
        "dextre_ids": array.array("i", [r[0] for r in dextre_raw]),
        "employees_ids": array.array("i", [r[0] for r in employees_raw]),
        "colors_ids_tolist": array.array("i", [r[0] for r in colors_raw]).tolist(),
        "dextre_ids_tolist": array.array("i", [r[0] for r in dextre_raw]).tolist(),
        "employees_ids_tolist": array.array("i", [r[0] for r in employees_raw]).tolist(),
    }

    # 5. DICTIONNAIRE (indexé par id + liste de dicts)
    dict_by_id = {
        "colors": {r[0]: {"id": r[0], "nom": r[1]} for r in colors_raw},
        "dextre": {r[0]: {"id": r[0], "type": r[1]} for r in dextre_raw},
        "employees": {r[0]: {"id": r[0], "nom": r[1], "prenom": r[2]} for r in employees_raw},
    }
    list_of_dicts = {
        "colors": [{"id": r[0], "nom": r[1]} for r in colors_raw],
        "dextre": [{"id": r[0], "type": r[1]} for r in dextre_raw],
        "employees": [{"id": r[0], "nom": r[1], "prenom": r[2]} for r in employees_raw],
    }

    # 6. SET / ENSEMBLE (valeurs uniques triées pour affichage déterministe)
    set_data = {
        "colors_noms": sorted({r[1] for r in colors_raw}),
        "dextre_types": sorted({r[1] for r in dextre_raw}),
        "employees_noms": sorted({r[1] for r in employees_raw}),
    }

    # 7. DEQUE (file double extrémité)
    deque_data = {
        "colors": list(deque(colors_raw)),
        "dextre": list(deque(dextre_raw)),
        "employees": list(deque(employees_raw)),
    }

    # 8. GROUPE (groupement par première lettre / champ)
    sorted_emp_by_nom = sorted(employees_raw, key=lambda x: (x[1] or "").lower())
    grouped_employees = {
        key: list(group)
        for key, group in groupby(sorted_emp_by_nom, key=lambda x: (x[1][:1].upper() if x[1] else "?"))
    }
    grouped_colors_len = {
        k: list(v)
        for k, v in groupby(sorted(colors_raw, key=lambda x: len(x[1] or "")), key=lambda x: len(x[1] or ""))
    }
    grouped_dextre_len = {
        k: list(v)
        for k, v in groupby(sorted(dextre_raw, key=lambda x: len(x[1] or "")), key=lambda x: len(x[1] or ""))
    }
    group_data = {
        "employees_par_initiale_nom": grouped_employees,
        "colors_par_longueur_nom": grouped_colors_len,
        "dextre_par_longueur_type": grouped_dextre_len,
    }

    # 9. ARBRE (structure arborescente base -> tables -> enregistrements -> colonnes)
    tree_data = {
        "database": "db_employees2",
        "tables": {
            "colors": {
                "type": "table",
                "children": [
                    {"node": f"color_{r[0]}", "leaves": {"id": r[0], "nom": r[1]}}
                    for r in colors_raw
                ],
            },
            "dextre": {
                "type": "table",
                "children": [
                    {"node": f"dextre_{r[0]}", "leaves": {"id": r[0], "type": r[1]}}
                    for r in dextre_raw
                ],
            },
            "employees": {
                "type": "table",
                "children": [
                    {
                        "node": f"employee_{r[0]}",
                        "leaves": {"id": r[0], "nom": r[1], "prenom": r[2]},
                    }
                    for r in employees_raw
                ],
            },
        },
    }

    # 10. JSON (sérialisation texte)
    json_payload = {
        "colors": list_of_dicts["colors"],
        "dextre": list_of_dicts["dextre"],
        "employees": list_of_dicts["employees"],
    }
    json_str = json.dumps(json_payload, indent=2, ensure_ascii=False)

    return {
        "liste": liste_data,
        "tuple": tuple_data,
        "namedtuple": namedtuple_data,
        "array": array_data,
        "dict_by_id": dict_by_id,
        "list_of_dicts": list_of_dicts,
        "set": set_data,
        "deque": deque_data,
        "group": group_data,
        "tree": tree_data,
        "json": json_str,
    }


HTML_TEMPLATE = """
<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Sandbox - Structures de données (3 tables)</title>
  {{ bootstrap.load_css() }}
  <style>
    pre {
      background: #f4f6f8;
      border: 1px solid #d0d7de;
      padding: 10px;
      font-size: 0.85rem;
      max-height: 360px;
      overflow: auto;
    }
  </style>
</head>
<body class="d-flex flex-column min-vh-100">

  <!-- HEADER -->
  <header class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Sandbox app2.py — Structures de données</a>
      <span class="navbar-text text-light">BD : db_employees2 (colors, dextre, employees)</span>
    </div>
  </header>

  <!-- MAIN -->
  <main class="container-fluid my-4 flex-grow-1">
    <p class="text-muted">Affichage brut des 3 tables dans différentes structures de données.</p>

    {% if error %}
      <div class="alert alert-danger">Erreur de connexion / requête : {{ error }}</div>
    {% else %}
      {% set s = data %}

      <!-- 1. LISTE -->
      <div class="card mb-4">
        <div class="card-header fw-bold">1. LISTE (list)</div>
        <div class="card-body">
          <strong>colors :</strong><pre>{{ s.liste.colors }}</pre>
          <strong>dextre :</strong><pre>{{ s.liste.dextre }}</pre>
          <strong>employees :</strong><pre>{{ s.liste.employees }}</pre>
        </div>
      </div>

      <!-- 2. TUPLE -->
      <div class="card mb-4">
        <div class="card-header fw-bold">2. TUPLE (tuple)</div>
        <div class="card-body">
          <strong>colors :</strong><pre>{{ s.tuple.colors }}</pre>
          <strong>dextre :</strong><pre>{{ s.tuple.dextre }}</pre>
          <strong>employees :</strong><pre>{{ s.tuple.employees }}</pre>
        </div>
      </div>

      <!-- 3. NAMEDTUPLE -->
      <div class="card mb-4">
        <div class="card-header fw-bold">3. NAMEDTUPLE (collections.namedtuple)</div>
        <div class="card-body">
          <strong>colors :</strong><pre>{{ s.namedtuple.colors }}</pre>
          <strong>dextre :</strong><pre>{{ s.namedtuple.dextre }}</pre>
          <strong>employees :</strong><pre>{{ s.namedtuple.employees }}</pre>
        </div>
      </div>

      <!-- 4. ARRAY -->
      <div class="card mb-4">
        <div class="card-header fw-bold">4. ARRAY (array.array('i', ids))</div>
        <div class="card-body">
          <strong>colors ids (repr / tolist) :</strong>
          <pre>{{ s.array.colors_ids }} -> {{ s.array.colors_ids_tolist }}</pre>
          <strong>dextre ids (repr / tolist) :</strong>
          <pre>{{ s.array.dextre_ids }} -> {{ s.array.dextre_ids_tolist }}</pre>
          <strong>employees ids (repr / tolist) :</strong>
          <pre>{{ s.array.employees_ids }} -> {{ s.array.employees_ids_tolist }}</pre>
        </div>
      </div>

      <!-- 5. DICTIONNAIRE -->
      <div class="card mb-4">
        <div class="card-header fw-bold">5. DICTIONNAIRE (dict indexé par id & liste de dicts)</div>
        <div class="card-body">
          <strong>dict[id] - colors :</strong><pre>{{ s.dict_by_id.colors }}</pre>
          <strong>dict[id] - dextre :</strong><pre>{{ s.dict_by_id.dextre }}</pre>
          <strong>dict[id] - employees :</strong><pre>{{ s.dict_by_id.employees }}</pre>
          <strong>liste de dicts (toutes les tables) :</strong><pre>{{ s.list_of_dicts }}</pre>
        </div>
      </div>

      <!-- 6. SET -->
      <div class="card mb-4">
        <div class="card-header fw-bold">6. ENSEMBLE / SET (valeurs uniques)</div>
        <div class="card-body">
          <strong>colors (noms uniques) :</strong><pre>{{ s.set.colors_noms }}</pre>
          <strong>dextre (types uniques) :</strong><pre>{{ s.set.dextre_types }}</pre>
          <strong>employees (noms uniques) :</strong><pre>{{ s.set.employees_noms }}</pre>
        </div>
      </div>

      <!-- 7. DEQUE -->
      <div class="card mb-4">
        <div class="card-header fw-bold">7. DEQUE (collections.deque)</div>
        <div class="card-body">
          <strong>colors :</strong><pre>{{ s.deque.colors }}</pre>
          <strong>dextre :</strong><pre>{{ s.deque.dextre }}</pre>
          <strong>employees :</strong><pre>{{ s.deque.employees }}</pre>
        </div>
      </div>

      <!-- 8. GROUPE -->
      <div class="card mb-4">
        <div class="card-header fw-bold">8. GROUPE (itertools.groupby)</div>
        <div class="card-body">
          <strong>employees groupés par initiale du nom :</strong>
          <pre>{{ s.group.employees_par_initiale_nom }}</pre>
          <strong>colors groupées par longueur du nom :</strong>
          <pre>{{ s.group.colors_par_longueur_nom }}</pre>
          <strong>dextre groupés par longueur du type :</strong>
          <pre>{{ s.group.dextre_par_longueur_type }}</pre>
        </div>
      </div>

      <!-- 9. ARBRE -->
      <div class="card mb-4">
        <div class="card-header fw-bold">9. ARBRE (structure hiérarchique + liste imbriquée HTML)</div>
        <div class="card-body">
          <strong>Arbre sous forme de dictionnaire/liste imbriquée :</strong>
          <pre>{{ s.tree }}</pre>
          <strong>Arbre visuel (UL / LI) :</strong>
          <ul>
            <li>{{ s.tree.database }}
              <ul>
                {% for tname, tval in s.tree.tables.items() %}
                  <li>{{ tname }}
                    <ul>
                      {% for child in tval.children %}
                        <li>{{ child.node }} -> {{ child.leaves }}</li>
                      {% endfor %}
                    </ul>
                  </li>
                {% endfor %}
              </ul>
            </li>
          </ul>
        </div>
      </div>

      <!-- 10. JSON -->
      <div class="card mb-4">
        <div class="card-header fw-bold">10. JSON (chaîne sérialisée)</div>
        <div class="card-body">
          <pre>{{ s.json }}</pre>
        </div>
      </div>

    {% endif %}
  </main>

  <!-- FOOTER -->
  <footer class="bg-light border-top py-3 text-center mt-auto">
    <div class="container-fluid">
      <small class="text-muted">Sandbox Flask + Bootstrap-Flask — app2.py</small>
    </div>
  </footer>

  {{ bootstrap.load_js() }}
</body>
</html>
"""


@app.route("/")
def index():
    try:
        colors_raw, dextre_raw, employees_raw = fetch_all_tables()
        structures = build_structures(colors_raw, dextre_raw, employees_raw)
        return render_template_string(HTML_TEMPLATE, data=structures, error=None)
    except Exception as exc:
        return render_template_string(HTML_TEMPLATE, data=None, error=str(exc))


if __name__ == "__main__":
    app.run(debug=True)