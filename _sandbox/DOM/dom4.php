<?php
// dom4.php — Image aléatoire avec Bootstrap 5 (PHP + Bootstrap + JS)
// Sources : Picsum, LoremFlickr, PlaceDog (gratuites, sans clé API) avec bascule automatique.

$largeur = 600;
$hauteur = 400;
?>
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DOM4 — Image aléatoire (Bootstrap)</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
  #zone-image {
    min-height: 300px;
    background: #e9ecef;
    position: relative;
  }
  #image-random { display: none; }
  #image-random.visible { display: block; }
</style>
</head>
<body class="bg-light">

<nav class="navbar navbar-dark bg-primary mb-4">
  <div class="container">
    <span class="navbar-brand mb-0 h1">DOM4 — Image aléatoire</span>
    <span class="badge text-bg-light" id="source-info">Chargement…</span>
  </div>
</nav>

<main class="container">
  <div class="row justify-content-center">
    <div class="col-12 col-md-10 col-lg-8">

      <div class="card shadow-sm">
        <div id="zone-image" class="d-flex align-items-center justify-content-center overflow-hidden card-img-top">
          <img id="image-random" class="img-fluid w-100" alt="Image aléatoire">
          <div id="spinner" class="spinner-border text-primary position-absolute d-none" role="status" style="width: 3rem; height: 3rem;">
            <span class="visually-hidden">Chargement...</span>
          </div>
        </div>

        <div class="card-body text-center">
          <h5 class="card-title">Découvre une image au hasard</h5>
          <p class="card-text text-muted">
            Clique sur le bouton ou appuie sur la touche <kbd>R</kbd>.
          </p>
          <button id="btn-random" type="button" class="btn btn-primary btn-lg">
            <span id="btn-spinner" class="spinner-border spinner-border-sm d-none" aria-hidden="true"></span>
            <span id="btn-texte">Charger une autre image</span>
          </button>
        </div>
      </div>

      <div id="alerte" class="alert mt-3 d-none" role="alert"></div>

    </div>
  </div>
</main>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script>
  const L = <?= (int)$largeur ?>;
  const H = <?= (int)$hauteur ?>;

  // Si une source échoue, on passe automatiquement à la suivante
  const SOURCES = [
    { nom: 'Lorem Picsum', url: (r) => `https://picsum.photos/${L}/${H}?random=${r}` },
    { nom: 'LoremFlickr',  url: (r) => `https://loremflickr.com/${L}/${H}?random=${r}` },
    { nom: 'PlaceDog',     url: (r) => `https://placedog.net/${L}/${H}?random&r=${r}` }
  ];

  const img        = document.getElementById('image-random');
  const bouton     = document.getElementById('btn-random');
  const btnTexte   = document.getElementById('btn-texte');
  const btnSpinner = document.getElementById('btn-spinner');
  const spinner    = document.getElementById('spinner');
  const alerte     = document.getElementById('alerte');
  const infoSrc    = document.getElementById('source-info');

  function setAlerte(texte, type) {
    alerte.textContent = texte;
    alerte.className = 'alert mt-3 alert-' + type;
  }

  function setChargement(actif) {
    bouton.disabled = actif;
    spinner.classList.toggle('d-none', !actif);
    btnSpinner.classList.toggle('d-none', !actif);
    btnTexte.textContent = actif ? 'Chargement...' : 'Charger une autre image';
  }

  function essayerSource(index, resolve, reject) {
    if (index >= SOURCES.length) { reject(); return; }

    const source  = SOURCES[index];
    const fantome = new Image();
    let termine   = false;

    const suivant = () => {
      if (termine) return;
      termine = true;
      clearTimeout(minuteur);
      essayerSource(index + 1, resolve, reject);
    };

    const minuteur = setTimeout(suivant, 6000);

    fantome.onload = () => {
      if (termine) return;
      termine = true;
      clearTimeout(minuteur);
      resolve({ src: fantome.src, nom: source.nom });
    };
    fantome.onerror = suivant;

    fantome.src = source.url(Date.now() + '' + Math.floor(Math.random() * 1000));
  }

  function chargerImage() {
    setChargement(true);
    alerte.classList.add('d-none');

    new Promise((resolve, reject) => essayerSource(0, resolve, reject))
      .then(({ src, nom }) => {
        img.src = src;
        img.classList.add('visible');
        infoSrc.textContent = 'Source : ' + nom;
        setAlerte('✅ Image chargée !', 'success');
      })
      .catch(() => {
        infoSrc.textContent = 'Aucune source';
        setAlerte('❌ Impossible de charger une image. Vérifie ta connexion, un bloqueur de pub ou ton pare-feu.', 'danger');
      })
      .finally(() => setChargement(false));
  }

  bouton.addEventListener('click', chargerImage);

  document.addEventListener('keydown', (e) => {
    if ((e.key === 'r' || e.key === 'R') && !bouton.disabled) chargerImage();
  });

  // Première image au chargement de la page
  chargerImage();
</script>

</body>
</html>