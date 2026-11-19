import json
from pathlib import Path
from flask import Flask, render_template_string
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

BASE_DIR = Path(__file__).resolve().parent
COLORS_FILE = BASE_DIR / "theme_colors.json"

DEFAULT_COLORS = {
    "header": {
        "bg": "#212529",
        "text": "#ffffff",
    },
    "footer": {
        "bg": "#f8f9fa",
        "text": "#212529",
    },
}


def load_theme_colors():
    """Charge les couleurs du header et du footer depuis theme_colors.json."""
    colors = {
        "header": dict(DEFAULT_COLORS["header"]),
        "footer": dict(DEFAULT_COLORS["footer"]),
    }
    if COLORS_FILE.exists():
        with COLORS_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        for section in ("header", "footer"):
            if isinstance(data.get(section), dict):
                colors[section].update(data[section])
    return colors


HTML_TEMPLATE = """
<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>app_json.py — Couleurs Header & Footer via JSON</title>
  {{ bootstrap.load_css() }}
  <style>
    .custom-header {
      background-color: {{ colors.header.bg }};
      color: {{ colors.header.text }};
    }
    .custom-header a,
    .custom-header .navbar-brand,
    .custom-header .nav-link {
      color: {{ colors.header.text }};
    }
    .custom-footer {
      background-color: {{ colors.footer.bg }};
      color: {{ colors.footer.text }};
    }
    .custom-footer a {
      color: {{ colors.footer.text }};
    }
  </style>
</head>
<body class="d-flex flex-column min-vh-100">

  <!-- HEADER -->
  <header class="navbar navbar-expand-lg custom-header border-bottom">
    <div class="container">
      <a class="navbar-brand fw-bold" href="/">MonApp JSON</a>
      <span class="navbar-text ms-auto" style="color: {{ colors.header.text }};">
        Header bg: {{ colors.header.bg }}
      </span>
    </div>
  </header>

  <!-- CONTENU -->
  <main class="container my-4 flex-grow-1">
    <h1>Header et Footer pilotés par JSON</h1>
    <p>Modifiez <code>theme_colors.json</code> puis rechargez la page pour voir les 2 couleurs changer.</p>
    <pre class="bg-light p-3 border rounded">{{ colors | tojson(indent=2) }}</pre>
  </main>

  <!-- FOOTER -->
  <footer class="custom-footer border-top py-3 text-center mt-auto">
    <div class="container">
      <span>Footer bg: {{ colors.footer.bg }} | Texte: {{ colors.footer.text }}</span>
    </div>
  </footer>

  {{ bootstrap.load_js() }}
</body>
</html>
"""


@app.route("/")
def index():
    colors = load_theme_colors()
    return render_template_string(HTML_TEMPLATE, colors=colors)


if __name__ == "__main__":
    app.run(debug=True)
    