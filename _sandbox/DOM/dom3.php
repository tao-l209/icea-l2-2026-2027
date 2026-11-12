<?php
// dom3.php — Image aléatoire avec bouton (PHP + CSS + JS)
// Sources : Picsum, LoremFlickr, PlaceDog (gratuites, sans clé API) avec bascule automatique.

$largeur = 600;
$hauteur = 400;
?>
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DOM3 — Image aléatoire</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
    background: #f5f6fa;
    color: #2c3e50;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 30px 15px;
  }

  h1 {
    font-size: 1.8rem;
    border-bottom: 3px solid #3498db;
    padding-bottom: 8px;
    margin-bottom: 6px;
  }

  .sous-titre {
    color: #7f8c8d;
    font-size: 0.95rem;
    margin-bottom: 25px;
  }

  #zone-image {
    width: 100%;
    max-width: 620px;
    min-height: 300px;
    background: #e8ecef;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    position: relative;
  }

  #image-random {
    max-width: 100%;
    height: auto;
    display: none;
    border-radius: 12px;
  }

  #image-random.visible { display: block; }

  #spinner {
    position: absolute;
    width: 48px;
    height: 48px;
    border: 5px solid #d0d7de;
    border-top-color: #3498db;
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
    display: none;
  }

  #spinner.actif { display: block; }

  @keyframes spin { to { transform: rotate(360deg); } }

  #btn-random {
    margin-top: 25px;
    padding: 13px 30px;
    border: none;
    border-radius: 8px;
    background: #3498db;
    color: white;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: background 0.2s, transform 0.15s, box-shadow 0.2s;
    box-shadow: 0 3px 10px rgba(52, 152, 219, 0.3);
  }

  #btn-random:hover:not(:disabled) {
    background: #2980b9;
    box-shadow: 0 5px 15px rgba(52, 152, 219, 0.4);
  }

  #btn-random:active:not(:disabled) { transform: scale(0.96); }

  #btn-random:disabled {
    background: #bdc3c7;
    cursor: wait;
    box-shadow: none;
  }

  #statut {
    margin-top: 15px;
    min-height: 22px;
    font-size: 14px;
    color: #7f8c8d;
    text-align: center;
  }

  #statut.ok     { color: #27ae60; }
  #statut.erreur { color: #e74c3c; }
</style>
</head>
<body>

<h1>Image aléatoire</h1>
<p class="sous-titre" id="source-info">Chargement de la source…</p>

<div id="zone-image">
  <img id="image-random" alt="Image aléatoire">
  <div id="spinner"></div>
</div>

<button id="btn-random">Charger une autre image</button>
<div id="statut"></div>

<script>
  const L = <?= (int)$largeur ?>;
  const H = <?= (int)$hauteur ?>;

  // Liste de sources : si l'une échoue, on passe à la suivante automatiquement
  const SOURCES = [
    { nom: 'Lorem Picsum', url: (r) => `https://picsum.photos/${L}/${H}?random=${r}` },
    { nom: 'LoremFlickr',  url: (r) => `https://loremflickr.com/${L}/${H}?random=${r}` },
    { nom: 'PlaceDog',     url: (r) => `https://placedog.net/${L}/${H}?random&r=${r}` }
  ];

  const img      = document.getElementById('image-random');
  const bouton   = document.getElementById('btn-random');
  const statut   = document.getElementById('statut');
  const spinner  = document.getElementById('spinner');
  const infoSrc  = document.getElementById('source-info');

  function setStatut(texte, type) {
    statut.textContent = texte;
    statut.className = type || '';
  }

  // Tente de charger l'image depuis la source n° "index", puis passe à la suivante en cas d'échec
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
    bouton.disabled = true;
    spinner.classList.add('actif');
    setStatut('Chargement...');

    new Promise((resolve, reject) => essayerSource(0, resolve, reject))
      .then(({ src, nom }) => {
        img.src = src;
        img.classList.add('visible');
        infoSrc.textContent = 'Source : ' + nom;
        setStatut('✅ Image chargée !', 'ok');
      })
      .catch(() => {
        infoSrc.textContent = 'Aucune source disponible';
        setStatut('❌ Impossible de charger une image. Vérifie ta connexion, un bloqueur de pub ou ton pare-feu.', 'erreur');
      })
      .finally(() => {
        spinner.classList.remove('actif');
        bouton.disabled = false;
      });
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